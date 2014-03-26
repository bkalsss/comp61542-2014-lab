from comp61542 import app
from database import database
from flask import (render_template, request)

def format_data(data):
    fmt = "%.2f"
    result = []
    for item in data:
        if type(item) is list:
            result.append(", ".join([ (fmt % i).rstrip('0').rstrip('.') for i in item ]))
        else:
            result.append((fmt % item).rstrip('0').rstrip('.'))
    return result

@app.route("/averages")
def showAverages():
    dataset = app.config['DATASET']
    db = app.config['DATABASE']
    args = {"dataset":dataset, "id":"averages"}
    args['title'] = "Averaged Data"
    tables = []
    headers = ["Average", "Conference Paper", "Journal", "Book", "Book Chapter", "All Publications"]
    averages = [ database.Stat.MEAN, database.Stat.MEDIAN, database.Stat.MODE ]
    tables.append({
        "id":1,
        "title":"Average Authors per Publication",
        "header":headers,
        "rows":[
                [ database.Stat.STR[i] ]
                + format_data(db.get_average_authors_per_publication(i)[1])
                for i in averages ] })
    tables.append({
        "id":2,
        "title":"Average Publications per Author",
        "header":headers,
        "rows":[
                [ database.Stat.STR[i] ]
                + format_data(db.get_average_publications_per_author(i)[1])
                for i in averages ] })
    tables.append({
        "id":3,
        "title":"Average Publications in a Year",
        "header":headers,
        "rows":[
                [ database.Stat.STR[i] ]
                + format_data(db.get_average_publications_in_a_year(i)[1])
                for i in averages ] })
    tables.append({
        "id":4,
        "title":"Average Authors in a Year",
        "header":headers,
        "rows":[
                [ database.Stat.STR[i] ]
                + format_data(db.get_average_authors_in_a_year(i)[1])
                for i in averages ] })

    args['tables'] = tables
    return render_template("averages.html", args=args)

@app.route("/coauthors")
def showCoAuthors():
    dataset = app.config['DATASET']
    db = app.config['DATABASE']
    PUB_TYPES = ["Conference Papers", "Journals", "Books", "Book Chapters", "All Publications"]
    args = {"dataset":dataset, "id":"coauthors"}
    args["title"] = "Co-Authors"

    start_year = db.min_year
    if "start_year" in request.args:
        start_year = int(request.args.get("start_year"))

    end_year = db.max_year
    if "end_year" in request.args:
        end_year = int(request.args.get("end_year"))

    pub_type = 4
    if "pub_type" in request.args:
        pub_type = int(request.args.get("pub_type"))

    args["data"] = db.get_coauthor_data(start_year, end_year, pub_type)
    args["start_year"] = start_year
    args["end_year"] = end_year
    args["pub_type"] = pub_type
    args["min_year"] = db.min_year
    args["max_year"] = db.max_year
    args["start_year"] = start_year
    args["end_year"] = end_year
    args["pub_str"] = PUB_TYPES[pub_type]
    return render_template("coauthors.html", args=args)

@app.route("/searchauthortofindcoauthors")
def showSearchAuthorToFindCoauthors():
    dataset = app.config['DATASET']
    db = app.config['DATABASE']
    args = {"dataset":dataset}
    args["title"] = "Search By Author"
    
    args["data"] = []

    data = []
    if "author" in request.args:
        author = request.args.get("author")
        args["author"] = author

#         get_coauthor_details = db.get_coauthor_details(author)
#         print len(get_coauthor_details)
#         for ix in get_coauthor_details:
#             if ix[0]!= author:
#                 print ix[0]
#                 data.append(ix[0])
        
        args["data"] = db.get_coauthor_list(author)
        print db.get_coauthor_list(author)
    return render_template('searchauthortofindcoauthors.html', args=args)

@app.route("/searchauthor")
def showSearchAuthor():
    dataset = app.config['DATASET']
    db = app.config['DATABASE']
    args = {"dataset":dataset}
    args["title"] = "Search By Author"
    
    author = None
    args["data"] = []
    
    if "author" in request.args:
        author = request.args.get("author")
        args["author"] = author
        print "ALALALALALALALALALALALALALALALALALALALALALALA"
        print  db.get_num_first_publications_by_author(author)
        get_publications_by_author = db.get_publications_by_author()
        
        for x in get_publications_by_author[1]:
            #print 'x --- ', x
            if author == x[0]:
                print 'x --- ', x[5]
                
                # get overall publications
                args["overallPublications"] = x[5]
                
                # get number of conference paper
                args["numConferencePaper"] = x[1]
                
                # get number of journal article
                args["numJournalArticle"] = x[2]
                
                # get number of book
                args["numBook"] = x[3]
                
                # get number of book chapters
                args["numBookChapters"] = x[4]
        
        get_network_data = db.get_network_data()
        
        print 'get_coauthor_details ----', get_network_data[0]
        for a, b in enumerate(get_network_data[0]):
            print 'b --- ', b
            if author == b[0]:
                args["numCoAuthors"] = b[1]
                get_first_publications_by_author = db.get_first_publications_by_author()
        
        for y in get_first_publications_by_author[1]:
            #print 'x --- ', x
            if author == y[0]:
            
                # total of author appeared first
                args["appearFirstAuthor"] = y[5]
                
        get_last_publications_by_author = db.get_last_publications_by_author()
        
        for z in get_last_publications_by_author[1]:
            #print 'x --- ', x
            if author == z[0]:
            
                # total of author appeared last
                args["appearLastAuthor"] = z[5]    

        
    return render_template('searchauthor.html', args=args)

@app.route("/")
def showStatisticsMenu():
    dataset = app.config['DATASET']
    args = {"dataset":dataset}
    return render_template('statistics.html', args=args)

@app.route("/soleauthor")
def showSoleAuthor():
    dataset = app.config['DATASET']
    db = app.config['DATABASE']
    args = {"dataset":dataset, "id":"soleauthors"}
    
    PUB_TYPES = ["Conference Papers", "Journals", "Books", "Book Chapters", "All Publications"]
    pub_type = 4
    if "pub_type" in request.args:
        pub_type = int(request.args.get("pub_type"))

    args["title"] = "Sole Author"
    args["data"] = db.get_sole_author(pub_type)    
    args["pub_str"] = PUB_TYPES[pub_type]    
    return render_template('soleauthor.html', args=args)    
        
@app.route("/statisticsdetails/<status>")
def showPublicationSummary(status):
    dataset = app.config['DATASET']
    db = app.config['DATABASE']
    args = {"dataset":dataset, "id":status}

    if (status == "publication_summary"):
        args["title"] = "Publication Summary"
        args["data"] = db.get_publication_summary()

    if (status == "publication_author"):
        args["title"] = "Author Publication"
        args["data"] = db.get_publications_by_author()

    if (status == "first_publication_author"):
        args["title"] = "First Author Publication"
        args["data"] = db.get_first_publications_by_author()

    if (status == "last_publication_author"):
        args["title"] = "Last Author Publication"
        args["data"] = db.get_last_publications_by_author()

    if (status == "publication_year"):
        args["title"] = "Publication by Year"
        args["data"] = db.get_publications_by_year()

#     if (status == "sole_author"):
#         PUB_TYPES = ["Conference Papers", "Journals", "Books", "Book Chapters", "All Publications"]
#         pub_type = 4
#         if "pub_type" in request.args:
#             pub_type = int(request.args.get("pub_type"))
#         args["pub_str"] = PUB_TYPES[pub_type]
#         args["title"] = "Sole Author"
#         args["data"] = db.get_sole_author()

    if (status == "author_year"):
        args["title"] = "Author by Year"
        args["data"] = db.get_author_totals_by_year()

    return render_template('statistics_details.html', args=args)
