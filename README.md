# 📜 API Documentation — Metro System

## Base URL

```
/api/v1/metro
```


## 🚇 Metro Routes

### 1. Get All Metro Lines

**Request:**

```
GET /lines
```

**Description:**
Retrieve all metro lines.

**Response — Success (200):**

```json
{
  "metro_lines": [
    "METRO 9",
    "METRO 13",
    "METRO 10",
    "METRO 6",
    "METRO 5",
    "METRO 2",
    "METRO 12",
    "METRO 7bis",
    "METRO 3bis",
    "METRO 1",
    "METRO 4",
    "METRO 8",
    "METRO 3",
    "METRO 14",
    "METRO 11",
    "METRO 7"
  ]
}
```

---

### 2. Get All Stations

**Request:**

```
GET /stations
```

**Description:**
Retrieve all metro stations.

**Response — Success (200):**

```json
{
  "data": {
    "stations": {
      "count": 322,
      "name": ["Abbesses", "Aimé Césaire", "Alexandre Dumas", "..."]
    }
  }
}
```

---

### 3. Get Stations by Metro Line

**Request:**

```
GET /lines/<metro_line>
```

**Description:**
Retrieve all stations of a specific metro line.

### **```metro_line``` values:**

```LINE 1```: 1

```LINE 2```: 2

```LINE 3```: 3

```LINE 3bis```: 3bis

```LINE 4```: 4

```LINE 5```: 5

```LINE 6```: 6

```LINE 7```: 7

```LINE 7bis```: 7b

```LINE 8```: 8

```LINE 9```: 9

```LINE 10```: 10

```LINE 11```: 11

```LINE 12```: 12

```LINE 13```: 13

```LINE 14```: 14


**Response — Success (200):**

```json
{
  "data": {
    "stations": {
      "count": 4,
      "locations": [
        {
          "lat": 48.86844016327547,
          "lon": 2.401561712742542
        },
        {
          "lat": 48.87711051176337,
          "lon": 2.40672924554309
        },
        {
          "lat": 48.87210144213156,
          "lon": 2.4045149423791043
        },
        {
          "lat": 48.86516343488149,
          "lon": 2.3987465934425916
        }
      ],
      "names": [
        "Gambetta",
        "Pelleport",
        "Porte des Lilas",
        "Saint-Fargeau"
      ]
    }
  },
  "img": "https://data.iledefrance-mobilites.fr/api/explore/v2.1/catalog/datasets/emplacement-des-gares-idf/files/84385f6415d8d60e0a135171e93312a5",
  "metro_line": "3bis",
  "operator": "RATP"
}
```

**Response — Error (404):**

```json
{
  "status": "error",
  "message": "provided metro line is unknown"
}
```

---

### 4. Get Metro Lines by Station

**Request:**

```
GET /stations/<station>/lines
```

**Description:**
Retrieve all metro lines passing through a specific station.

### **```station```values:**

```71545``` : Porte de Clichy

```70721``` : Boulogne - Pont de Saint-Cloud

```71840``` : Goncourt

```72203``` : Gabriel Péri

```71125``` : Pasteur

```71350``` : Notre-Dame-de-Lorette

```71201``` : Sully-Morland

```71084``` : Porte de Saint-Cloud

```71864``` : Pyrénées

```71359``` : Gare de l'Est

```71139``` : Montparnasse-Bienvenüe

```71911``` : Pré Saint-Gervais

```71227``` : Rue du Bac

```70990``` : Corentin Celton

```71086``` : Lourmel

```71135``` : Gare d'Austerlitz

```73626``` : Gare de Lyon

```71264``` : Châtelet

```71092``` : Saint-Marcel

```70143``` : Villejuif - Louis Aragon

```73671``` : Monceau

```71972``` : Ourcq

```71639``` : Picpus

```71416``` : Malesherbes

```474152``` : Porte Dauphine

```71284``` : Tuileries

```474149``` : Château-Landon

```479928``` : Buzenval

```71469``` : Château Rouge

```71410``` : Gare du Nord

```71056``` : Denfert-Rochereau

```71673``` : Nation

```71694``` : Rue des Boulets

```463564``` : Bastille

```73651``` : Chevaleret

```71148``` : Jussieu

```71510``` : Marx Dormoy

```72118``` : Mairie de Clichy

```73653``` : Mouton-Duvernet

```71337``` : Opéra

```71157``` : Ségur

```71170``` : Vaneau

```71817``` : Gallieni

```73696``` : La Courneuve 8 Mai 1945

```71697``` : Avron

```71556``` : Simplon

```71296``` : Temple

```71403``` : Villiers

```73753``` : Chevilly - Larue

```73635``` : Bourse

```473829``` : Bir-Hakeim

```73617``` : Europe

```71190``` : Maubert-Mutualité

```71492``` : Lamarck-Caulaincourt

```71558``` : Liberté

```71043``` : Nationale

```71885``` : Place des Fêtes

```73640``` : Rennes

```71311``` : République

```71117``` : Vavin

```70248``` : Villejuif Paul Vaillant-Couturier

```71781``` : Saint-Ambroise

```71475``` : Pont Cardinet

```71370``` : Saint-Lazare

```71420``` : Blanche

```426280``` : Rosny-Bois-Perrier

```478860``` : Villejuif - Gustave Roussy

```71453``` : Pereire-Levallois

```73650``` : Bel-Air

```71614``` : Daumesnil

```71026``` : Glacière

```71511``` : Marcadet-Poissonniers

```71199``` : La Motte Picquet-Grenelle

```70452``` : Le Kremlin-Bicêtre

```73618``` : Odéon

```71217``` : Pont Marie

```71088``` : Raspail

```71216``` : Saint-Germain-des-Prés

```71795``` : Rue Saint-Maur

```73794``` : Les Halles

```70657``` : Porte d'Orléans

```74041``` : Front Populaire

```71001``` : Tolbiac

```71528``` : Guy Môquet

```71435``` : Place de Clichy

```71961``` : Stalingrad

```63284``` : Aéroport d'Orly

```474150``` : La Muette

```71347``` : Charles De Gaulle-Étoile

```482368``` : Havre-Caumartin

```71132``` : Commerce

```71206``` : Michel Ange-Auteuil

```71076``` : Les Gobelins

```71324``` : Madeleine

```70488``` : Mairie d'Ivry

```71870``` : Télégraphe

```73656``` : Kléber

```71815``` : Ménilmontant

```72013``` : Crimée

```71940``` : Jaurès

```69884``` : Créteil - Pointe du Lac

```490779``` : Serge Gainsbourg

```71828``` : Pelleport

```70586``` : Mairie de Montrouge

```71150``` : Javel - André Citroën

```72326``` : Basilique de Saint-Denis

```73622``` : Chemin Vert

```71124``` : Exelmans

```71889``` : Porte des Lilas

```72128``` : Garibaldi

```71750``` : Voltaire

```71075``` : Convention

```73620``` : Saint-Michel

```71318``` : Franklin D. Roosevelt

```71725``` : Robespierre

```71407``` : Louis Blanc

```71108``` : Edgar Quinet

```71147``` : Boulogne - Jean Jaurès

```71519``` : Anatole France

```71223``` : Cité

```71703``` : Maraîchers

```71297``` : Palais Royal - Musée du Louvre

```71803``` : Oberkampf

```71654``` : Reuilly-Diderot

```71156``` : Charles Michels

```70562``` : Malakoff - Rue Étienne Dolet

```71162``` : Mirabeau

```71382``` : Liège

```71777``` : Saint-Sébastien-Froissart

```71285``` : Trocadéro

```71063``` : Campo Formio

```71330``` : Richelieu-Drouot

```71301``` : Boissière

```71634``` : Château de Vincennes

```71292``` : Rue de la Pompe

```71860``` : Saint-Fargeau

```71204``` : Saint-François-Xavier

```72064``` : Porte de la Chapelle

```73642``` : Assemblée Nationale

```415852``` : Hôtel de Ville

```73766``` : Malakoff - Plateau de Vanves

```71363``` : Poissonnière

```72024``` : Église de Pantin

```71333``` : Château d'Eau

```70445``` : Hôpital Bicêtre

```71013``` : Corvisart

```71808``` : Gambetta

```71693``` : Ledru Rollin

```71159``` : Duroc

```71728``` : Alexandre Dumas

```71853``` : Belleville

```71197``` : Dupleix

```425779``` : Les Sablons

```71006``` : Porte de Vanves

```72004``` : Hoche

```71315``` : Victor Hugo

```71277``` : Filles du Calvaire

```71242``` : La Tour Maubourg

```71045``` : Porte de Versailles

```71041``` : Saint-Jacques

```72039``` : Bobigny-Pantin - Raymond Queneau

```71426``` : Barbès-Rochechouart

```71434``` : La Chapelle

```412992``` : Boucicaut

```71328``` : George V

```71322``` : Jacques Bonsergent

```71787``` : Père Lachaise

```71039``` : Plaisance

```70596``` : Porte d'Italie

```73788``` : Pyramides

```478883``` : Porte de Clignancourt

```71977``` : Riquet

```73689``` : Chaussée d'Antin - La Fayette

```490782``` : La Dhuys

```71320``` : Bonne Nouvelle

```72126``` : Saint-Ouen

```71834``` : Couronnes

```71893``` : Colonel Fabien

```71054``` : Marcel Sembat

```71203``` : Sèvres-Babylone

```71663``` : Porte de Vincennes

```71751``` : Philippe Auguste

```71351``` : Cadet

```71947``` : Romainville - Carnot

```69974``` : L'Haÿ - les - Roses

```71557``` : Olympiades

```71137``` : Félix Faure

```71647``` : Saint-Mandé

```71141``` : Chardon Lagache

```73619``` : Cluny-La Sorbonne

```71293``` : Arts et Métiers

```71167``` : Cambronne

```71298``` : Concorde

```74001``` : Faidherbe Chaligny

```71474``` : La Fourche

```71710``` : Porte de Montreuil

```70636``` : Porte d'Ivry

```71597``` : Quai de la Gare

```71799``` : Porte de Bagnolet

```71367``` : Ternes

```71637``` : Quai de la Rapée

```73633``` : Strasbourg-Saint-Denis

```72491``` : Aimé Césaire

```70645``` : Maison Blanche

```71290``` : Alma-Marceau

```71576``` : Cour Saint-Émilion

```461505``` : Châtillon-Montrouge

```71346``` : Miromesnil

```71273``` : Rambuteau

```71366``` : Saint-Georges

```70269``` : Créteil–L’Échat

```71326``` : Grands Boulevards

```71073``` : Balard

```71909``` : Mairie des Lilas

```71432``` : Abbesses

```71305``` : Champs-Élysées – Clemenceau

```73639``` : Mabillon

```71379``` : Porte Maillot

```490784``` : Saint-Denis – Pleyel

```71521``` : Jules Joffrin

```71355``` : Trinité d'Estienne d'Orves

```72031``` : Corentin Cariou

```72486``` : Bobigny Pablo Picasso

```71030``` : Alésia

```70172``` : Créteil-Université

```73661``` : Brochant

```72217``` : Carrefour Pleyel

```73641``` : Falguière

```478885``` : Le Peletier

```71237``` : Passy

```71313``` : Quatre Septembre

```72285``` : Saint-Denis - Porte de Paris

```72286``` : Les Courtilles

```71785``` : Mairie de Montreuil

```71409``` : Pigalle

```71169``` : Porte d'Auteuil

```70648``` : Charenton-Écoles

```71158``` : Avenue Émile Zola

```73657``` : Jasmin

```73658``` : Michel Ange-Molitor

```71232``` : Varenne

```71450``` : Porte de Champerret

```69677``` : Thiais - Orly

```71033``` : Place d'Italie

```73621``` : Bréguet-Sabin

```70522``` : École Vétérinaire de Maisons-Alfort

```73667``` : Louise Michel

```71801``` : Parmentier

```71133``` : Place Monge

```70604``` : Porte de Choisy

```71144``` : Sèvres-Lecourbe

```72078``` : Porte de Saint-Ouen

```72358``` : Saint-Denis - Université

```71113``` : Volontaires

```70426``` : Maisons-Alfort-Stade

```71607``` : Bercy

```72168``` : Mairie de Saint-Ouen

```71224``` : École Militaire

```71897``` : Montreuil - Hôpital

```71153``` : Cardinal Lemoine

```71868``` : Jourdain

```412687``` : Pernety

```70537``` : Pierre et Marie Curie

```71334``` : Saint-Philippe du Roule

```73636``` : Réaumur Sébastopol

```71442``` : Pont de Neuilly

```72430``` : Porte de la Villette

```71274``` : Invalides

```71270``` : Solférino

```71139``` : Montparnasse Bienvenüe

```71202``` : Saint-Sulpice

```71348``` : Argentine

```72460``` : Aubervilliers Pantin - Quatre Chemins

```71166``` : Église d'Auteuil

```73630``` : Louvre-Rivoli

```71222``` : Saint-Paul

```72240``` : Les Agnettes

```71253``` : Pont Neuf

```72057``` : Pont de Levallois

```70358``` : Maisons-Alfort-Les Juilliottes

```70021``` : Créteil–Préfecture

```71595``` : Michel Bizot

```71138``` : Notre-Dame-des-Champs

```73648``` : Richard Lenoir

```71243``` : Ranelagh

```71572``` : Bibliothèque François Mitterrand

```71034``` : Billancourt

```73675``` : Gaîté

```71184``` : Saint-Placide

```479068``` : Étienne Marcel

```71989``` : Porte de Pantin

```71756``` : Croix de Chavaux

```71957``` : Laumière

```73634``` : Sentier

```71419``` : Anvers

```71376``` : Courcelles

```70441``` : Barbara

```71920``` : Bolivar

```71650``` : Bérault

```73695``` : Fort d'Aubervilliers

```71100``` : Censier-Daubenton

```73690``` : Saint-Augustin

```483315``` : Bagneux - Lucie Aubrac

```72524``` : Mairie d'Aubervilliers

```73647``` : Charonne

```71485``` : Esplanade de la Défense

```71517``` : La Défense

```71606``` : Dugommier

```71900``` : Buttes-Chaumont

```71423``` : Wagram

```71091``` : Vaugirard

```71631``` : Montgallet

```70375``` : Villejuif - Léo Lagrange

```70671``` : Mairie d'Issy

```71591``` : Porte Dorée

```490783``` : Coteaux Beauclair

```71906``` : Botzaris

```71930``` : Danube

```71294``` : Iéna

```70698``` : Pont de Sèvres

```71579``` : Porte de Charenton

```71408``` : Rome

**Response — Success (200):**

```json
{
  "data": {
    "lines": {
      "count": 1,
      "names": [
        "METRO 4"
      ],
      "picto": [
        "https://data.iledefrance-mobilites.fr/api/explore/v2.1/catalog/datasets/emplacement-des-gares-idf/files/40edb03ba8639ac2542ee899469bacdb"
      ]
    }
  },
  "location": [
    {
      "lat": 48.83111266037533,
      "lon": 2.3297050126201846
    }
  ],
  "operator": "RATP",
  "station": "Mouton-Duvernet"
}
```

**Response — Error (404):**

```json
{
  "status": "error",
  "message": "Unknown station"
}
```
