import mysql.connector
import numpy as np

config = {
  'user': 'root',
  'password': 'root',
  'host': '127.0.0.1',
  'port': 3306,
  'database': 'trees',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cursor = cnx.cursor(dictionary=True)

cursor.execute("SELECT id, name  FROM Clients")

results = cursor.fetchall()

for row in results:
  id = row['id']
  title = row['name']
  print '%s | %s' % (id, title)

cnx.close()

total_f = cursor.execute("SELECT COUNT(id) FROM Freelancers")
total_c = cursor.execute("SELECT COUNT(id) FROM Clients")

def table_freelancers_creation():
    table_f = total_f*[NULL]
    for i in range (total_f) :
        table_f[i] = cursor.execute("SELECT name FROM Freelancers WHERE id = i")


def table_clients_creation():
    table_c = total_c*[NULL]
    for i in range (total_c) :
        table_c[i] = cursor.execute("SELECT name FROM Clients WHERE id=i")


def eliminatory_comparison():
    for i in range(total_c):
        for j in range(total_f):
            industry_c = cursor.execute("SELECT industry FROM Clients WHERE id=j")
            industry_f = cursor.execute("SELECT industry FROM Freelancers WHERE id=i")
            subindustry_c = cursor.execute("SELECT subindustry FROM Clients WHERE id=j")
            subindustry_f = cursor.execute("SELECT subindustry FROM Freelancers WHERE id=i")
            discipline_c = cursor.execute("SELECT discipline FROM Clients WHERE id=j")
            discipline_f = cursor.execute("SELECT discipline FROM Freelancers WHERE id=i")
            position_c = cursor.execute("SELECT position FROM Clients WHERE id=j")
            position_f = cursor.execute("SELECT position FROM Freelancers WHERE id=i")
            deliverable_type_c = cursor.execute("SELECT deliverable type FROM Clients WHERE id=j")
            deliverable_type_f = cursor.execute("SELECT deliverable type FROM Freelancers WHERE id=i")
            if industry_f =! industry_c :
                score[i][j] = 0
            else if subindustry_f =! subindustry_c :
                score[i][j] = 0
            else if discipline_f =! discipline_c :
                score[i][j] = 0
            else if position_f =! position_c :
                score[i][j] = 0
            else if deliverable_type_f =! deliverable_type_c :
                score[i][j] = 0
            else :
                Print(cursor.execute("SELECT name FROM Freelancers WHERE id=i",'n'est pas éliminé pour le CLient' j)

def eliminatory(table[][]):
    for i in range(total_c):
        for j in range(total_f):
            if score[i][j]= 0 :
                table = np.delete (table, [i,j])
    print("Les Freelancers non éliminés sont les suivants ",table)


def freelancer_restant(table[][]):
    freelancer = eliminatory(table[][])
    return freelancer

def score_aftereliminatory(table[][]):
    table = eliminatory(table[][]) ##NOM DES FREELANCERS NON ELIMINES
    score = total_f*[NULL]
    for i in range (total_c) :
        for j in range(total_f):
            name_freelancer = cursor.execute("SELECT name FROM Freelancers WHERE id=j")
            if eliminatory[j][i] == name_freelancer:
                score [i][j] = score[i][j] + 10
            else :
                score [i][j] = 0
    print ("Les scores des Freelancers après éliminations sont les suivants", score)



scoretotal_freelance = np.empty(total_c,total_f)



def score_software(a,b):
    if isinstance(a,(int)) and isinstance(b,(int)) and a<=total_c and b<=total_f:
        score = 0
        table_software_c = [cursor.execute("SELECT software FROM Clients WHERE id=a")]
        l = len(table_software_c)
        table_software_f = [cursor.execute("SELECT software FROM Freelancers WHERE id=b")]
        m = len(table_software_f)
        if l > 0 :
            for i in range (l):
                for j in range (m):
                    if table_software_f[j] == table_software_c[i] :
                        score = score + 1
                    else :
                        j += 1
                    scoretotal_freelance [i][j] = scoretotal_freelance [i][j] + (score/l)*5


def score_role(a,b):
    if isinstance(a,(int)) and isinstance(b,(int)) and a<=total_c and b<=total_f:
        table_role_c = [cursor.execute("SELECT role FROM Clients WHERE id=a")]
        l = len(table_role_c)
        table_role_f = [cursor.execute("SELECT role FROM Freelancers WHERE id=b")]
        m = len(table_role_f)
        for i in range (l) :
            for j in range (m):
                if table_role_c[i] == table_role_f[j] :
                    score = score + 1
                else :
                    j+=1
                scoretotal_freelance [i][j] = scoretotal_freelance [i][j] + (score/l)*5

def score_experience(a,b):
    if isinstance(a,(int)) and isinstance(b,(int)) and a<=total_c and b<=total_f:
        table_experience_c = [cursor.execute("SELECT experience FROM Clients WHERE id=a")]
        table_experience_f = [cursor.execute("SELECT experience` FROM `Freelancers WHERE id=b")]
        l = len(table_experience_c)
        m = len(table_experience_f)
        for i in range (l) :
            for j in range (m):
                if table_experience_c[i] == table_experience_f[j] :
                    score = score + 1
                else :
                    j+=1
                scoretotal_freelance [i][j] = scoretotal_freelance [i][j] + (score/l)*5

def score_projectphase(a,b):
    if isinstance(a,(int)) and isinstance(b,(int)) and a<=total_c and b<=total_f:
        table_projectphase_c = [cursor.execute("SELECT projectphase FROM Clients WHERE id=a")]
        l = len(table_projectphase_c)
        table_projectphase_f = [cursor.execute("SELECT projetphase FROM Freelancers WHERE id = b")]
        m = len(table_projectphase_f)
        for i in range (l) :
            for j in range (m):
                if table_projectphase_c[i] == table_projectphase_[j] :
                    score = score + 1
                else :
                    j+=1
                scoretotal_freelance [i][j] = scoretotal_freelance [i][j] + (score/l)*4

def score_productline(a,b):
    if isinstance(a,(int)) and isinstance(b,(int)) and a<=total_c and b<=total_f:
        table_productline_c = [cursor.execute("SELECT productline FROM Clients WHERE id=a")]
        l = len(table_productline_c)
        table_productline_f = [cursor.execute("SELECT productline FROM Freelancers WHERE id=b")]
        m = len(table_productline_f)
        for i in range (l) :
            for j in range (m):
                if table_productline_c[i] == table_productline_f[j] :
                    score = score + 1
                else :
                    j+=1
                scoretotal_freelance [i][j] = scoretotal_freelance [i][j] + (score/l)*2

def score_producttype(a,b):
    if isinstance(a,(int)) and isinstance(b,(int)) and a<=total_c and b<=total_f:
        table_producttype_c = [cursor.execute("SELECT producttype FROM Clients WHERE id=a")]
        l = len(table_producttype_c)
        table_producttype_f = [cursor.execute("SELECT producttype FROM Freelancers WHERE id=b")]
        m = len(table_producttype_f)
        for i in range (l) :
            for j in range (m):
                if table_producttype_c[i] == table_producttype_f[j] :
                    score = score + 1
                else :
                    j+=1
                scoretotal_freelance [i][j] = scoretotal_freelance [i][j] + (score/l)*2

def score_deliverablename(a,b):
    if isinstance(a,(int)) and isinstance(b,(int)) and a<=total_c and b<=total_f:
        table_deliverablename_c = [cursor.execute("SELECT deliverablename FROM Clients WHERE id=a")]
        l = len(table_deliverablename_c)
        table_deliverablename_f = [cursor.execute("SELECT deliverablename FROM Freelancers WHERE id=b")]
        m = len(table_deliverablename_f)
        for i in range (l) :
            for j in range (m):
                if table_deliverablename_c[i] == table_deliverablename_f[j] :
                    score = score + 1
                else :
                    j+=1
                scoretotal_freelance [i][j] = scoretotal_freelance [i][j] + (score/l)*5

def score_taskkeywords(a,b):
    if isinstance(a,(int)) and isinstance(b,(int)) and a<=total_c and b<=total_f:
        table_taskkeywords_c = [cursor.execute("SELECT taskkeywords FROM Clients WHERE id=a")]
        l = len(table_taskkeywords_c)
        table_taskkeywords_f = [cursor.execute("SELECT taskkeywords FROM Freelancers WHERE id=b")]
        m = len(table_taskkeywords_f)
        for i in range (l) :
            for j in range (m):
                if table_taskkeywords_c[i] == table_taskkeywords_f[j] :
                    score = score + 1
                else :
                    j+=1
                scoretotal_freelance [i][j] = scoretotal_freelance [i][j] + (score/l)*5



def score_codesandstandards(a,b):
    if isinstance(a,(int)) and isinstance(b,(int)) and a<=total_c and b<=total_f:
        table_codesandstandards_c = [cursor.execute("SELECT codesandstandards FROM Clients WHERE id=a")]
        l = len(table_codesandstandards_c)
        table_codesandstandards_f = [cursor.execute("SELECT codesandstandards FROM Freelancers WHERE id=b")]
        m = len(table_codesandstandards_f)
        for i in range (l) :
            for j in range (m):
                if table_codesandstandards_c[i] == table_codesandstandards_f[j] :
                    score = score + 1
                else :
                    j+=1
                scoretotal_freelance[i][j] = scoretotal_freelance[i][j] + (score/l)*4



def maximum_ligne(mat):
    if mat.shape[0] = 2:
        maxi = mat[1][0]
        index_maxi = 0
        for i in range(total_f):
            if mat[1][i] >= maxi:
                maxi = mat[1][i]
                index_maxi = i
    return (maxi,index_maxi)
    else :
        print("La matrice",mat,"est mal choisie")

def resultats_match(a):
    if isinstance(a,(int)) and a<=total_c:
        table_resultats = np.empty(2,(total_f))
        table_freelancer = np.empty(2,(total_f))
        for j in range(total_f):
            table_freelancer[1][j] = scoretotal_freelance[a][j]
            table_freelancer[0][j] = cursor.execute("SELECT name FROM Freelancers WHERE id=j")
        while len(table_freelancer.shape)>0 :
            b = 0
            for i in range(total_f):
                maximum_ligne(table_freelancer) = (table_resultats[1][i],b)
                table_resultats[0][i] = cursor.execute("SELECT name FROM Freelancers WHERE id=b")
                np.delete(table_freelancer,b,1)
    print ("Les Freelancers les plus adaptés pour le Client",a,"sont les suivants",table_resultats)







