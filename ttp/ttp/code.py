import pandas as pd
df = pd.read_csv("fr-esr-parcoursup.csv",sep = ";")

liste_filiere_agregee = list(df["Filière de formation très agrégée"].unique())
liste_region = list(df["Région de l’établissement"].unique())
liste_etablissement = list(df["Établissement"].unique())
liste_de_filiere = list(df["Filière de formation"].unique())

def moyenne_gen_pro_tech(filiere):
    df_prepa = df[df["Filière de formation"]==filiere]
    df_prepa = df_prepa[["Filière de formation très agrégée","Filière de formation","Filière de formation détaillée bis","LIB_FOR_VOE_INS","Région de l’établissement","Commune de l’établissement","Département de l’établissement","Établissement",r"% d’admis néo bacheliers généraux",r"% d’admis néo bacheliers professionnels",r"% d’admis néo bacheliers technologiques"]]
    #print(display(df_prepa))
    return df_prepa

def moyenne_selon_filiere(filiere):
    """Les filières sont general pro ou techno"""

    if filiere == "pro":
        return moyenne_filiere(df_moyenne_pro,r"% d’admis néo bacheliers professionnels")
    elif filiere == "general":
        return moyenne_filiere(df_moyenne_general,r"% d’admis néo bacheliers généraux")
    else:
        return moyenne_filiere(df_moyenne_techno,r"% d’admis néo bacheliers technologiques")


def moyenne_par_formation_detaillee(formation):
  """Les formations sont DCG, prepa... (il y en a 51)"""
  return moyenne_gen_pro_tech(formation)
  
def moyenne_par_formation_agregee(formation):
  """Ces formations sont : (il y en a 11)
  'Autre formation', 'BTS', 'BUT', 'CPGE', 'Licence', "Ecole d'Ingénieur", 'Ecole de Commerce', 'IFSI', 'EFTS', 'PASS', 'Licence_Las'"""
  df_prepa = df[df["Filière de formation très agrégée"]==formation]
  df_prepa = df_prepa[["Filière de formation très agrégée","Filière de formation","Filière de formation détaillée bis","LIB_FOR_VOE_INS","Région de l’établissement","Commune de l’établissement","Département de l’établissement","Établissement",r"% d’admis néo bacheliers généraux",r"% d’admis néo bacheliers professionnels",r"% d’admis néo bacheliers technologiques"]]
  #print(display(df_prepa))
  return df_prepa
def moyenne_par_filiere_bis(filiere):
  
  df_prepa = df[df["Filière de formation"]==filiere]
  df_prepa = df_prepa[["Filière de formation très agrégée","Filière de formation","Filière de formation détaillée bis","LIB_FOR_VOE_INS","Région de l’établissement","Commune de l’établissement","Département de l’établissement","Établissement",r"% d’admis néo bacheliers généraux",r"% d’admis néo bacheliers professionnels",r"% d’admis néo bacheliers technologiques"]]
  return df_prepa

def moyenne_par_etablissement(etablissement):
  """Les établissements sont les noms exactes (il y en a 3505). 
  Il faudrait rajouter un code permettant de retrouver un établissement selon la recherche d'un utilisateur """
  df_prepa = df[df["Établissement"]==etablissement]
  df_prepa = df_prepa[["Filière de formation très agrégée","Filière de formation","Filière de formation détaillée bis","LIB_FOR_VOE_INS","Région de l’établissement","Commune de l’établissement","Département de l’établissement","Établissement",r"% d’admis néo bacheliers généraux",r"% d’admis néo bacheliers professionnels",r"% d’admis néo bacheliers technologiques"]]
  return df_prepa
def moyenne_par_region(region):
  """Il y a 21 régions différentes"""
  df_prepa = df[df["Région de l’établissement"]==region]
  df_prepa = df_prepa[["Filière de formation très agrégée","Filière de formation","Filière de formation détaillée bis","LIB_FOR_VOE_INS","Région de l’établissement","Commune de l’établissement","Département de l’établissement","Établissement",r"% d’admis néo bacheliers généraux",r"% d’admis néo bacheliers professionnels",r"% d’admis néo bacheliers technologiques"]]
  return df_prepa

def moyenne_par_region_et_formation(region,formation):
  df_prepa = df[df["Région de l’établissement"]==region]
  df_prepa = df_prepa[df_prepa["Filière de formation"] == formation]
  df_prepa = df_prepa[["Filière de formation très agrégée","Filière de formation","Filière de formation détaillée bis","LIB_FOR_VOE_INS","Région de l’établissement","Commune de l’établissement","Département de l’établissement","Établissement",r"% d’admis néo bacheliers généraux",r"% d’admis néo bacheliers professionnels",r"% d’admis néo bacheliers technologiques"]]
  return df_prepa
def moyenne_par_ville_et_formation(region,formation):
  df_prepa = df[df["Commune de l’établissement"]==region]
  df_prepa = df_prepa[df_prepa["Filière de formation"] == formation]
  df_prepa = df_prepa[["Filière de formation très agrégée","Filière de formation","Filière de formation détaillée bis","LIB_FOR_VOE_INS","Région de l’établissement","Commune de l’établissement","Département de l’établissement","Établissement",r"% d’admis néo bacheliers généraux",r"% d’admis néo bacheliers professionnels",r"% d’admis néo bacheliers technologiques"]]
  return df_prepa
def moyenne_par_departement_et_formation(region,formation):
  df_prepa = df[df["Département de l’établissement"]==region]
  df_prepa = df_prepa[df_prepa["Filière de formation"] == formation]
  df_prepa = df_prepa[["Filière de formation très agrégée","Filière de formation","Filière de formation détaillée bis","LIB_FOR_VOE_INS","Région de l’établissement","Commune de l’établissement","Département de l’établissement","Établissement",r"% d’admis néo bacheliers généraux",r"% d’admis néo bacheliers professionnels",r"% d’admis néo bacheliers technologiques"]]
  return df_prepa
def moyenne_par_region_et_formation_agregee(region,formation):
  df_prepa = df[df["Région de l’établissement"]==region]
  df_prepa = df_prepa[df_prepa["Filière de formation très agrégée"] == formation]
  df_prepa = df_prepa[["Filière de formation très agrégée","Filière de formation","Filière de formation détaillée bis","LIB_FOR_VOE_INS","Région de l’établissement","Commune de l’établissement","Département de l’établissement","Établissement",r"% d’admis néo bacheliers généraux",r"% d’admis néo bacheliers professionnels",r"% d’admis néo bacheliers technologiques"]]
  return df_prepa
def moyenne_par_ville_et_formation_agregee(region,formation):
  df_prepa = df[df["Commune de l’établissement"]==region]
  df_prepa = df_prepa[df_prepa["Filière de formation très agrégée"] == formation]
  df_prepa = df_prepa[["Filière de formation très agrégée","Filière de formation","Filière de formation détaillée bis","LIB_FOR_VOE_INS","Région de l’établissement","Commune de l’établissement","Département de l’établissement","Établissement",r"% d’admis néo bacheliers généraux",r"% d’admis néo bacheliers professionnels",r"% d’admis néo bacheliers technologiques"]]
  return df_prepa
def moyenne_par_departement_et_formation_agregee(region,formation):
  df_prepa = df[df["Département de l’établissement"]==region]
  df_prepa = df_prepa[df_prepa["Filière de formation très agrégée"] == formation]
  df_prepa = df_prepa[["Filière de formation très agrégée","Filière de formation","Filière de formation détaillée bis","LIB_FOR_VOE_INS","Région de l’établissement","Commune de l’établissement","Département de l’établissement","Établissement",r"% d’admis néo bacheliers généraux",r"% d’admis néo bacheliers professionnels",r"% d’admis néo bacheliers technologiques"]]
  return df_prepa
def moyenne_par_ville(region):
  """Il y a 21 régions différentes"""
  df_prepa = df[df["Commune de l’établissement"]==region]
  df_prepa = df_prepa[["Filière de formation très agrégée","Filière de formation","Filière de formation détaillée bis","LIB_FOR_VOE_INS","Région de l’établissement","Commune de l’établissement","Département de l’établissement","Établissement",r"% d’admis néo bacheliers généraux",r"% d’admis néo bacheliers professionnels",r"% d’admis néo bacheliers technologiques"]]
  return df_prepa
def moyenne_par_departement(region):
  """Il y a 21 régions différentes"""
  df_prepa = df[df["Département de l’établissement"]==region]
  df_prepa = df_prepa[["Filière de formation très agrégée","Filière de formation","Filière de formation détaillée bis","LIB_FOR_VOE_INS","Région de l’établissement","Commune de l’établissement","Département de l’établissement","Établissement",r"% d’admis néo bacheliers généraux",r"% d’admis néo bacheliers professionnels",r"% d’admis néo bacheliers technologiques"]]
  return df_prepa

def moyenne_par_region_et_formation_bis(region,formation_bis):
  df_prepa = df[df["Région de l’établissement"]==region]
  
  df_prepa = df_prepa[df_prepa["Filière de formation détaillée bis"] == formation_bis]
  df_prepa = df_prepa[["Filière de formation très agrégée","Filière de formation","Filière de formation détaillée bis","LIB_FOR_VOE_INS","Région de l’établissement","Commune de l’établissement","Département de l’établissement","Établissement",r"% d’admis néo bacheliers généraux",r"% d’admis néo bacheliers professionnels",r"% d’admis néo bacheliers technologiques"]]
  return df_prepa
def moyenne_par_departement_et_formation_bis(departement,formation_bis):
  df_prepa = df[df["Département de l’établissement"]==departement]
  
  df_prepa = df_prepa[df_prepa["Filière de formation détaillée bis"] == formation_bis]
  df_prepa = df_prepa[["Filière de formation très agrégée","Filière de formation","Filière de formation détaillée bis","LIB_FOR_VOE_INS","Région de l’établissement","Commune de l’établissement","Département de l’établissement","Établissement",r"% d’admis néo bacheliers généraux",r"% d’admis néo bacheliers professionnels",r"% d’admis néo bacheliers technologiques"]]
  return df_prepa
def moyenne_par_ville_et_formation_bis(ville,formation_bis):
  df_prepa = df[df["Commune de l’établissement"]==ville]
  
  df_prepa = df_prepa[df_prepa["Filière de formation détaillée bis"] == formation_bis]
  df_prepa = df_prepa[["Filière de formation très agrégée","Filière de formation","Filière de formation détaillée bis","LIB_FOR_VOE_INS","Région de l’établissement","Commune de l’établissement","Département de l’établissement","Établissement",r"% d’admis néo bacheliers généraux",r"% d’admis néo bacheliers professionnels",r"% d’admis néo bacheliers technologiques"]]
  return df_prepa

def moyenne_par_formation_bis(filiere):
  
  df_prepa = df[df["Filière de formation détaillée bis"]==filiere]
  df_prepa = df_prepa[["Filière de formation très agrégée","Filière de formation","Filière de formation détaillée bis","LIB_FOR_VOE_INS","Région de l’établissement","Commune de l’établissement","Département de l’établissement","Établissement",r"% d’admis néo bacheliers généraux",r"% d’admis néo bacheliers professionnels",r"% d’admis néo bacheliers technologiques"]]
  return df_prepa

#moyenne_par_region_et_formation("Ile-de-France","Classe préparatoire économique et commerciale")
#moyenne_par_formation_detaillee("DCG")
#moyenne_par_etablissement("Lycée Newton-Enrea")
#moyenne_par_region("Ile-de-France")
#moyenne_par_formation_agregee("Ecole de Commerce")
#moyenne_par_region_et_formation_agregee("Ile-de-France","CPGE")
#moyenne_par_ville("Marseille")

liste_lieux = []

liste_de_regions = list(df["Région de l’établissement"].unique())
liste_departement = list(df["Département de l’établissement"].unique())
liste_ville = list(df["Commune de l’établissement"].unique())
for reg in liste_de_regions:
    if reg not in liste_lieux:
        liste_lieux.append(reg)
for dep in liste_departement:
    if dep not in liste_lieux:
        liste_lieux.append(dep)
for ville in liste_ville:
    if ville not in liste_lieux:
        liste_lieux.append(ville)
def trouver_lieu_existant(dtfrm):
    liste_lieux = []

    liste_de_regions = list(dtfrm["Région de l’établissement"].unique())
    liste_departement = list(dtfrm["Département de l’établissement"].unique())
    liste_ville = list(dtfrm["Commune de l’établissement"].unique())
    for reg in liste_de_regions:
        if reg not in liste_lieux:
            liste_lieux.append(reg)
    for dep in liste_departement:
        if dep not in liste_lieux:
            liste_lieux.append(dep)
    for ville in liste_ville:
        if ville not in liste_lieux:
            liste_lieux.append(ville)
    liste_lieux = sorted(liste_lieux)
    return liste_lieux
def probas(dfi):    
    proba_g = str(round(dfi["% d’admis néo bacheliers généraux"].mean(),2))+" %"
    proba_p = str(round(dfi["% d’admis néo bacheliers professionnels"].mean(),2))+" %"
    proba_t = str(round(dfi["% d’admis néo bacheliers technologiques"].mean(),2))+" %"
    t_uple = (proba_g,proba_p,proba_t)
    return t_uple
nul = ('nan %', 'nan %', 'nan %')

def affichage(lieu,choix_dep,choix_ville,choix_fil):
  premiere_liste = liste_filiere_agregee
  if lieu == "":
        
        df1 = moyenne_par_formation_agregee(choix_dep)        
        df2 = moyenne_par_formation_detaillee(choix_ville)        
        df3 = moyenne_par_formation_bis(choix_fil)
        liste_place_df1 = trouver_lieu_existant(df1)
        liste_place_df2 = trouver_lieu_existant(df2)
        liste_place_df3 = trouver_lieu_existant(df3)
        first_df2 = ""
        first_df3 = ""
        precedent_df3 = ""
        li_df1 = ""
        li_df2 = ""
        li_df3_from_one = ""
        li_df3_from_two = ""
        if len(df1)!=0:
          li_df2 = list(df1["Filière de formation"].unique())
          li_df2 = sorted(li_df2)
          li_df3_from_one = list(df1["Filière de formation détaillée bis"].unique())
          li_df3_from_one = sorted(li_df3_from_one)
          
        #li_formation = list(df1["Filière de formation"].unique())
        if len(df2)!=0:
          first_df2 = list(df2["Filière de formation très agrégée"].unique())[0]
          li_df3_from_two = list(df2["Filière de formation détaillée bis"].unique())
          li_df3_from_two = sorted(li_df3_from_two)
        if len(df3)!=0:
          first_df3 = list(df3["Filière de formation très agrégée"].unique())[0]
          precedent_df3 = list(df3["Filière de formation"].unique())[0]
        suivant = "Selection"     

        
        
        li_df1 = sorted(li_df1)
        
        

        return probas(df1),probas(df2),probas(df3),first_df2,first_df3,precedent_df3,suivant,liste_place_df1,liste_place_df2,liste_place_df3,li_df1,li_df2,li_df3_from_one,li_df3_from_two,premiere_liste
  
  else:
      """On crée 3 dataframes vides"""
      df1 = moyenne_par_region("")
      df2 = moyenne_par_region("")
      df3 = moyenne_par_region("")
    
      df1_region = moyenne_par_region_et_formation_agregee(lieu,choix_dep)
      df1_dep = moyenne_par_departement_et_formation_agregee(lieu,choix_dep)
      df1_ville = moyenne_par_ville_et_formation_agregee(lieu,choix_dep)

      df2_region = moyenne_par_region_et_formation(lieu,choix_ville)
      df2_dep = moyenne_par_departement_et_formation(lieu,choix_ville)
      df2_ville = moyenne_par_ville_et_formation(lieu,choix_ville)

      df3_region = moyenne_par_region_et_formation_bis(lieu,choix_fil)
      df3_dep = moyenne_par_departement_et_formation_bis(lieu,choix_fil)
      df3_ville = moyenne_par_ville_et_formation_bis(lieu,choix_fil)

      first_df2 = ""
      first_df3 = ""
      precedent_df3 = ""

      li_df3_from_one = ""
      li_df3_from_two = ""
      
      
      if len(df1_region)!=0:
        df1 = df1_region
      elif len(df1_dep)!=0:
        df1 = df1_dep
      elif len(df1_ville)!=0:
        df1 = df1_ville
      
      if len(df2_region)!=0:
        df2 = df2_region
      elif len(df2_dep)!=0:
        df2 = df2_dep
      elif len(df2_ville)!=0:
        df2 = df2_ville

      if len(df3_region)!=0:
        df3 = df3_region
      elif len(df1_dep)!=0:
        df3 = df3_dep
      elif len(df3_ville)!=0:
        df3 = df3_ville

      df_reg = moyenne_par_region(lieu)
      df_depa = moyenne_par_departement(lieu)
      df_vil = moyenne_par_ville(lieu)
      df_lieu = df_vil
      if len(df_reg)!=0:
        df_lieu = df_reg
      elif len(df_depa)!=0:
          df_lieu = df_depa
      elif len(df_vil)!=0:
          df_lieu = df_vil
      li_df1 = list(df_lieu["Filière de formation très agrégée"].unique())
      li_df1 = sorted(li_df1)
      li_df2 = list(df_lieu["Filière de formation"].unique())
      li_df2 = sorted(li_df2)
      li_df3_from_one = list(df_lieu["Filière de formation détaillée bis"].unique())
      li_df3_from_one = sorted(li_df3_from_one)

      if len(df2)!=0:
        first_df2 = list(df2["Filière de formation très agrégée"].unique())[0]
      if len(df3)!=0:
        first_df3 = list(df3["Filière de formation très agrégée"].unique())[0]
        precedent_df3 = list(df3["Filière de formation"].unique())[0]
      suivant = "Selection" 


      if len(df1)!=0:
        li_df2 = list(df1["Filière de formation"].unique())
        li_df2 = sorted(li_df2)
        li_df3_from_one = list(df1["Filière de formation détaillée bis"].unique())
        li_df3_from_one = sorted(li_df3_from_one)
        
      #li_formation = list(df1["Filière de formation"].unique())
      if len(df2)!=0:
        first_df2 = list(df2["Filière de formation très agrégée"].unique())[0]
        li_df3_from_two = list(df2["Filière de formation détaillée bis"].unique())
        li_df3_from_two = sorted(li_df3_from_two)
      if len(df3)!=0:
        first_df3 = list(df3["Filière de formation très agrégée"].unique())[0]
        precedent_df3 = list(df3["Filière de formation"].unique())[0]
       
      
      """
      li_df2 = list(df_lieu["Filière de formation"].unique())
      li_df3_from_one = list(df_lieu["Filière de formation détaillée bis"].unique())
      li_df1 = sorted(li_df1)
      li_df2 = sorted(li_df2)
      li_df3_from_one = sorted(li_df3_from_one)
      """

      df1_edit = moyenne_par_formation_agregee(choix_dep)        
      df2_edit = moyenne_par_formation_detaillee(choix_ville)        
      df3_edit = moyenne_par_formation_bis(choix_fil)
      liste_place_df1 = trouver_lieu_existant(df1_edit)
      liste_place_df2 = trouver_lieu_existant(df2_edit)
      liste_place_df3 = trouver_lieu_existant(df3_edit)
      #li_df3_from_two = li_df3_from_one
      return probas(df1),probas(df2),probas(df3),first_df2,first_df3,precedent_df3,suivant,liste_place_df1,liste_place_df2,liste_place_df3,li_df1,li_df2,li_df3_from_one,li_df3_from_two,premiere_liste




      



def affichage_old(lieu,choix_dep,choix_ville,choix_fil):
    
    if lieu != "" and choix_dep!="Selection" and choix_ville=="Selection" and choix_fil=="Selection" :
        dfi = moyenne_par_region_et_formation_agregee(lieu,choix_dep)
        if len(dfi)!=0:
            li = list(dfi["Filière de formation"].unique())
            suivant = "Selection"
            precedent = ""
            return probas(dfi),li,precedent,suivant
        else:
            dfi = moyenne_par_departement_et_formation_agregee(lieu,choix_dep)
            if len(dfi)!=0:
                li = list(dfi["Filière de formation"].unique())
                suivant = "Selection"
                precedent = ""
                return probas(dfi),li,precedent,suivant
            else:
                dfi = moyenne_par_ville_et_formation_agregee(lieu,choix_dep)
                if len(dfi)!=0:
                  li = list(dfi["Filière de formation"].unique())
                  suivant = "Selection"
                  precedent = ""
                  return probas(dfi),li,precedent,suivant
                else:
                  li = list(dfi["Filière de formation"].unique())
                  suivant = "Selection"
                  precedent = "Selection"
                  return nul,li,precedent,suivant

    elif lieu != "" and choix_dep!="Selection" and choix_ville!="Selection" and choix_fil=="Selection" :
        dfi = moyenne_par_region_et_formation(lieu,choix_ville)
        if len(dfi)!=0:
            li = list(dfi["Filière de formation"].unique())
            first = list(dfi["Filière de formation très agrégée"].unique())[0]
            precedent = first
            suivant = "Selection"
            return probas(dfi),li,precedent,suivant,first
        else:
            dfi = moyenne_par_departement_et_formation(lieu,choix_ville)
            if len(dfi)!=0:
                li = list(dfi["Filière de formation"].unique())
                first = list(dfi["Filière de formation très agrégée"].unique())[0]
                precedent = first
                suivant = "Selection"
                return probas(dfi),li,precedent,suivant,first
            else:
                dfi = moyenne_par_ville_et_formation(lieu,choix_ville)
                if len(dfi)!=0:
                  li = list(dfi["Filière de formation"].unique())
                  first = list(dfi["Filière de formation très agrégée"].unique())[0]
                  suivant = "Selection"
                  return probas(dfi),li,precedent,suivant,first
                else:
                  li = list(dfi["Filière de formation"].unique())
                  first = list(dfi["Filière de formation très agrégée"].unique())[0]
                  suivant = "Selection"
                  precedent = "Selection"
                  return nul,li,precedent,suivant,first

    elif lieu != "" and choix_dep!="Selection" and choix_ville!="Selection" and choix_fil!="Selection" :
        dfi = moyenne_par_region_et_formation_bis(lieu,choix_fil)
        if len(dfi)!=0:
            li = list(dfi["Filière de formation"].unique())
            precedent = list(dfi["Filière de formation"].unique())[0]
            first = list(dfi["Filière de formation très agrégée"].unique())[0]
            suivant = "Selection"            
            return probas(dfi),li,precedent,suivant,first
        else:
            dfi = moyenne_par_departement_et_formation_bis(lieu,choix_fil)
            if len(dfi)!=0:
                li = list(dfi["Filière de formation"].unique())
                precedent = list(dfi["Filière de formation"].unique())[0]
                first = list(dfi["Filière de formation très agrégée"].unique())[0]
                suivant = "Selection"
                return probas(dfi),li,precedent,suivant,first
            else:
                dfi = moyenne_par_ville_et_formation_bis(lieu,choix_fil)
                if len(dfi)!=0:
                  li = list(dfi["Filière de formation"].unique())
                  precedent = list(dfi["Filière de formation"].unique())[0]
                  first = list(dfi["Filière de formation très agrégée"].unique())[0]
                  suivant = "Selection"
                  return probas(dfi),li,precedent,suivant,first
                else:
                  li = list(dfi["Filière de formation"].unique())
                  first = "Selection"
                  suivant = "Selection"
                  precedent = "Selection"
                  return nul,li,precedent,suivant,first

    elif lieu != "" and choix_dep=="Selection" and choix_ville!="Selection" and choix_fil=="Selection" :
        dfi = moyenne_par_region_et_formation(lieu,choix_ville)
        if len(dfi)!=0:
            li = list(dfi["Filière de formation"].unique())
            first = list(dfi["Filière de formation très agrégée"].unique())[0]
            precedent = first
            suivant = "Selection"
            return probas(dfi),li,precedent,suivant,first
        else:
            dfi = moyenne_par_departement_et_formation(lieu,choix_ville)
            if len(dfi)!=0:
                li = list(dfi["Filière de formation"].unique())
                first = list(dfi["Filière de formation très agrégée"].unique())[0]
                precedent = first
                suivant = "Selection"
                return probas(dfi),li,precedent,suivant,first
            else:
                dfi = moyenne_par_ville_et_formation(lieu,choix_ville)
                if len(dfi)!=0:
                  li = list(dfi["Filière de formation"].unique())
                  first = list(dfi["Filière de formation très agrégée"].unique())[0]
                  suivant = "Selection"
                  return probas(dfi),li,precedent,suivant,first
                else:
                  li = list(dfi["Filière de formation"].unique())
                  first = list(dfi["Filière de formation très agrégée"].unique())[0]
                  suivant = "Selection"
                  precedent = "Selection"
                  return nul,li,precedent,suivant,first
       


    elif lieu != "" and choix_dep=="Selection" and choix_ville=="Selection" and choix_fil!="Selection" :
        
      
        dfi = moyenne_par_region_et_formation_bis(lieu,choix_fil)
        if len(dfi)!=0:
            li = list(dfi["Filière de formation"].unique())
            precedent = list(dfi["Filière de formation"].unique())[0]
            first = list(dfi["Filière de formation très agrégée"].unique())[0]
            suivant = "Selection"            
            return probas(dfi),li,precedent,suivant,first
        else:
            dfi = moyenne_par_departement_et_formation_bis(lieu,choix_fil)
            if len(dfi)!=0:
                li = list(dfi["Filière de formation"].unique())
                precedent = list(dfi["Filière de formation"].unique())[0]
                first = list(dfi["Filière de formation très agrégée"].unique())[0]
                suivant = "Selection"
                return probas(dfi),li,precedent,suivant,first
            else:
                dfi = moyenne_par_ville_et_formation_bis(lieu,choix_fil)
                if len(dfi)!=0:
                  li = list(dfi["Filière de formation"].unique())
                  precedent = list(dfi["Filière de formation"].unique())[0]
                  first = list(dfi["Filière de formation très agrégée"].unique())[0]
                  suivant = "Selection"
                  return probas(dfi),li,precedent,suivant,first
                else:
                  li = list(dfi["Filière de formation"].unique())
                  first = list(dfi["Filière de formation très agrégée"].unique())[0]
                  suivant = "Selection"
                  precedent = "Selection"
                  return nul,li,precedent,suivant,first

    elif lieu != "" and choix_dep!="Selection" and choix_ville=="Selection" and choix_fil!="Selection" :
        
      
        dfi = moyenne_par_region_et_formation_bis(lieu,choix_fil)
        if len(dfi)!=0:
            li = list(dfi["Filière de formation"].unique())
            precedent = list(dfi["Filière de formation"].unique())[0]
            first = list(dfi["Filière de formation très agrégée"].unique())[0]
            suivant = "Selection"   
                 
            return probas(dfi),li,precedent,suivant,first
        else:
            dfi = moyenne_par_departement_et_formation_bis(lieu,choix_fil)
            if len(dfi)!=0:
                li = list(dfi["Filière de formation"].unique())
                precedent = list(dfi["Filière de formation"].unique())[0]
                first = list(dfi["Filière de formation très agrégée"].unique())[0]
                suivant = "Selection"
                return probas(dfi),li,precedent,suivant,first
            else:
                dfi = moyenne_par_ville_et_formation_bis(lieu,choix_fil)
                if len(dfi)!=0:
                  li = list(dfi["Filière de formation"].unique())
                  precedent = list(dfi["Filière de formation"].unique())[0]
                  first = list(dfi["Filière de formation très agrégée"].unique())[0]
                  suivant = "Selection"
                  return probas(dfi),li,precedent,suivant,first
                else:
                  li = list(dfi["Filière de formation"].unique())
                  first = list(dfi["Filière de formation très agrégée"].unique())[0]
                  suivant = "Selection"
                  precedent = "Selection"
                  return nul,li,precedent,suivant,first

    elif lieu != "" and choix_dep=="Selection" and choix_ville!="Selection" and choix_fil!="Selection" :
        
      
        dfi = moyenne_par_region_et_formation_bis(lieu,choix_fil)
        if len(dfi)!=0:
            li = list(dfi["Filière de formation"].unique())
            precedent = list(dfi["Filière de formation"].unique())[0]
            first = list(dfi["Filière de formation très agrégée"].unique())[0]
            suivant = "Selection"   
                 
            return probas(dfi),li,precedent,suivant,first
        else:
            dfi = moyenne_par_departement_et_formation_bis(lieu,choix_fil)
            if len(dfi)!=0:
                li = list(dfi["Filière de formation"].unique())
                precedent = list(dfi["Filière de formation"].unique())[0]
                first = list(dfi["Filière de formation très agrégée"].unique())[0]
                suivant = "Selection"
                return probas(dfi),li,precedent,suivant,first
            else:
                dfi = moyenne_par_ville_et_formation_bis(lieu,choix_fil)
                if len(dfi)!=0:
                  li = list(dfi["Filière de formation"].unique())
                  precedent = list(dfi["Filière de formation"].unique())[0]
                  first = list(dfi["Filière de formation très agrégée"].unique())[0]
                  suivant = "Selection"
                  return probas(dfi),li,precedent,suivant,first
                else:
                  li = list(dfi["Filière de formation"].unique())
                  first = list(dfi["Filière de formation très agrégée"].unique())[0]
                  suivant = "Selection"
                  precedent = "Selection"
                  return nul,li,precedent,suivant,first


    

    elif lieu == "" and choix_dep!="Selection" and choix_ville=="Selection" and choix_fil=="Selection" :
        dfi = moyenne_par_formation_agregee(choix_dep)        
        li = list(dfi["Filière de formation"].unique())
        suivant = "Selection"
        precedent = ""
        return probas(dfi),li,precedent,suivant
        
    elif lieu == "" and choix_dep!="Selection" and choix_ville!="Selection" and choix_fil=="Selection" :
        dfi = moyenne_par_formation_detaillee(choix_ville)        
        li = list(dfi["Filière de formation"].unique())
        first = list(dfi["Filière de formation très agrégée"].unique())[0]
        precedent = first
        suivant = "Selection"
        return probas(dfi),li,precedent,suivant,first
    
    elif lieu == "" and choix_dep!="Selection" and choix_ville!="Selection" and choix_fil!="Selection" :
        a = choix_dep
        b = choix_ville
        c = choix_fil
        dfi = moyenne_par_formation_bis(choix_fil)        
        li = list(dfi["Filière de formation"].unique())
        precedent = list(dfi["Filière de formation"].unique())[0]
        first = list(dfi["Filière de formation très agrégée"].unique())[0]
        suivant = "Selection"            
        if choix_dep!=a:
          dfi = moyenne_par_formation_agregee(choix_dep)        
          li = list(dfi["Filière de formation"].unique())
          suivant = "Selection"
          precedent = ""
          return probas(dfi),li,precedent,suivant
        elif choix_ville != b:
          dfi = moyenne_par_formation_detaillee(choix_ville)        
          li = list(dfi["Filière de formation"].unique())
          precedent = list(dfi["Filière de formation"].unique())[0]
          first = list(dfi["Filière de formation très agrégée"].unique())[0]
          suivant = "Selection"            
          return probas(dfi),li,precedent,suivant,first
        

        return probas(dfi),li,precedent,suivant,first

    elif lieu == "" and choix_dep!="Selection" and choix_ville!="Selection" and choix_fil=="Selection" :
        dfi = moyenne_par_formation_detaillee(choix_ville)        
        li = list(dfi["Filière de formation"].unique())
        precedent = list(dfi["Filière de formation"].unique())[0]
        first = list(dfi["Filière de formation très agrégée"].unique())[0]
        suivant = "Selection"            
        return probas(dfi),li,precedent,suivant,first

    elif lieu == "" and choix_dep=="Selection" and choix_ville=="Selection" and choix_fil!="Selection" :
        dfi = moyenne_par_formation_bis(choix_fil)        
        li = list(dfi["Filière de formation"].unique())
        precedent = list(dfi["Filière de formation"].unique())[0]
        first = list(dfi["Filière de formation très agrégée"].unique())[0]
        suivant = "Selection"            
        return probas(dfi),li,precedent,suivant,first

    elif lieu == "" and choix_dep=="Selection" and choix_ville!="Selection" and choix_fil=="Selection" :
        dfi = moyenne_par_formation_detaillee(choix_ville)        
        li = list(dfi["Filière de formation"].unique())
        precedent = list(dfi["Filière de formation"].unique())[0]
        first = list(dfi["Filière de formation très agrégée"].unique())[0]
        suivant = "Selection"            
        return probas(dfi),li,precedent,suivant,first
    elif lieu == "" and choix_dep!="Selection" and choix_ville=="Selection" and choix_fil!="Selection" :
        dfi = moyenne_par_formation_bis(choix_fil)        
        li = list(dfi["Filière de formation"].unique())
        precedent = list(dfi["Filière de formation"].unique())[0]
        first = list(dfi["Filière de formation très agrégée"].unique())[0]
        suivant = "Selection"            
        return probas(dfi),li,precedent,suivant,first

    

    
    
        






    


        
def change_deroulante(lieu,choix_dep,choix_ville,choix_fil):
  pass

