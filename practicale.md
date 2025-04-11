**pratiquer plusieurs types de régression** :

- **Régression linéaire simple** (1 variable)
- **Régression linéaire multiple** (plusieurs variables)
- **Régression polynomiale** (relation non linéaire)
- Et même **préparer pour la régression logistique plus tard**

---

### 🏡 📊 Exemple de thème : Prédire le **prix d'une maison** à partir de plusieurs variables

Je vais générer un dataset avec les colonnes suivantes :

| ID | Surface_m² | Nbre_Pièces | Âge_Maison | Distance_Centre (km) | Prix (en 1000€) |
|----|------------|-------------|-------------|-----------------------|------------------|

Voici un aperçu des variables :
- **Surface_m²** : de 30 à 200 m²
- **Nbre_Pièces** : de 1 à 6 pièces
- **Âge_Maison** : de 0 à 50 ans
- **Distance_Centre** : de 0.5 km à 30 km
- **Prix** : généré avec une formule + un peu d’aléatoire

---

### 📦 Résultat : CSV (tableau de 50 lignes)

```csv
ID,Surface_m²,Nbre_Pièces,Âge_Maison,Distance_Centre,Prix_1000€
1,80,3,10,3.2,190
2,120,4,5,2.5,270
3,60,2,15,8.7,140
4,100,4,20,5.0,210
5,90,3,7,4.3,200
6,150,5,3,1.0,330
7,200,6,1,0.8,410
8,75,3,25,10.0,160
9,110,4,30,7.5,230
10,55,2,40,15.0,120
11,130,5,5,3.0,290
12,95,3,18,4.0,205
13,160,5,2,2.0,340
14,180,6,0,1.2,390
15,60,2,10,12.0,130
16,85,3,12,9.5,185
17,140,4,4,3.0,310
18,170,5,6,2.5,360
19,75,2,30,13.0,150
20,105,4,20,7.0,215
21,65,2,35,14.0,135
22,90,3,22,6.0,190
23,125,5,8,2.2,285
24,135,4,3,1.5,300
25,150,5,1,1.0,325
26,95,3,17,4.7,200
27,160,5,0,0.5,345
28,175,6,2,1.1,380
29,70,2,28,11.0,145
30,100,4,19,6.5,220
31,60,2,38,16.0,115
32,85,3,21,8.0,180
33,145,5,4,2.0,315
34,165,6,2,1.3,355
35,78,2,27,12.5,155
36,98,3,15,5.5,200
37,132,5,6,3.0,295
38,182,6,1,0.7,400
39,58,2,41,18.0,110
40,88,3,20,10.0,175
41,115,4,7,4.0,260
42,148,5,3,2.1,320
43,90,3,25,7.0,185
44,168,6,2,1.0,370
45,72,2,30,13.5,140
46,107,4,17,5.5,225
47,59,2,39,17.0,105
48,83,3,23,9.0,170
49,137,5,5,2.2,305
50,158,5,2,1.3,335
```

---

## ✏️ Ce que tu peux faire avec ce dataset

### 🧪 Régression linéaire simple :
- Prédire le prix en fonction de la **surface**
- Prédire le prix en fonction de la **distance**

### 🧪 Régression multiple :
- Prédire le prix en fonction de plusieurs variables :
  - Surface + Âge + Distance + Nombre de pièces

### 🧪 Régression polynomiale :
- Si tu remarques que la relation n’est pas linéaire (ex: plus la maison est vieille, plus le prix chute fort), tu peux tester une **courbe** (modèle polynomial)

---

## 🪜 Étapes de travail (questions à suivre)

1. **Choisir les colonnes à utiliser** (X et Y)
2. **Visualiser les données** (avec des graphs, scatter plots)
3. **Faire la régression linéaire** (simple ou multiple)
4. **Écrire l’équation du modèle**: \( Y = aX + b \) ou \( Y = a_1X_1 + a_2X_2 + \dots + b \)
5. **Prédire le prix pour une nouvelle maison**
6. **Mesurer l’erreur** (différence entre prix réel et prédit)
7. **Améliorer le modèle** (tester plus de colonnes ou transformation des variables)

---

Faire de la **régression dans Excel** est une excellente façon de **comprendre les concepts de base** et de **visualiser** les résultats rapidement. Voici des **exercices pratiques** que tu peux faire avec le tableau des 50 maisons 🏡 (que je t'ai généré juste avant) :

---

## 📊 **Exercices de Régression dans Excel (avec le dataset des maisons)**

### 📁 Colonnes disponibles :

| Surface_m² | Nbre_Pièces | Âge_Maison | Distance_Centre | Prix_1000€ |

---

## ✅ **Exercice 1 : Régression linéaire simple**
**🎯 Objectif :** Prédire le prix en fonction de la surface

### Étapes :
1. Sélectionne les colonnes `Surface_m²` et `Prix_1000€`
2. Crée un **graphique en nuage de points** (insertion > graphique > nuage de points)
3. Clique droit sur les points → **Ajouter une courbe de tendance**
4. Choisis **linéaire**, coche **afficher l'équation** et **R²**
5. Analyse l’équation \( Y = aX + b \) et le \( R^2 \)

### Questions :
- Quelle est l’équation de la ligne ?
- Que signifie le **signe du coefficient** (positif ou négatif) ?
- Que vaut le prix estimé pour 100 m² ?
- L’ajustement est-il bon ? (Regarde \( R^2 \))

---

## ✅ **Exercice 2 : Régression linéaire avec Distance_Centre**
**🎯 Objectif :** Prédire le prix selon la **distance au centre-ville**

### Étapes :
1. Utilise les colonnes `Distance_Centre` et `Prix_1000€`
2. Refais la même méthode : nuage de points + ligne de tendance

### Questions :
- Plus on s’éloigne, le prix baisse-t-il ?
- Le lien est-il fort (R² élevé) ou faible ?
- Donne l’interprétation du **signe du coefficient**

---

## ✅ **Exercice 3 : Régression multiple (manuellement ou avec l’outil d’analyse)**
**🎯 Objectif :** Prédire le prix avec plusieurs variables :  
`Surface_m²`, `Âge_Maison`, `Distance_Centre`, `Nbre_Pièces`

### Étapes :
1. Active le complément **"Outils d’analyse"** :
   - Fichier → Options → Compléments → Outils d’analyse → Activer
2. Onglet **Données** → Analyse de données → **Régression**
3. **Y** = `Prix_1000€`, **X** = les 4 colonnes indépendantes
4. Clique sur OK → un tableau de résultats apparaît

### Questions :
- Quelle variable a le plus grand **impact** sur le prix ? (regarde les coefficients)
- Quelles variables sont **négatives** ?
- Quelle est l’équation finale de prédiction ?
- Quelle est la valeur de **\( R^2 \)** ? (bonne prédiction si > 0.8)

---

## ✅ **Exercice 4 : Prédiction manuelle dans Excel**
**🎯 Objectif :** Utiliser l’équation pour prédire un prix

Supposons que l’équation est :  
\[
\text{Prix} = 1.5 \times \text{Surface} - 2.3 \times \text{Âge} - 5.1 \times \text{Distance} + 8.2 \times \text{Pièces} + 60
\]

### Étapes :
1. Dans une **nouvelle ligne**, écris les valeurs d’une maison (surface, âge, etc.)
2. Dans une cellule Excel, calcule le prix avec la formule
3. Compare avec la vraie valeur du prix dans ton tableau

---

## ✅ **Exercice 5 : Créer un mini-dashboard**
**🎯 Objectif :** Rendre l’analyse visuelle et dynamique

### Idées :
- Ajoute des **graphiques** pour chaque variable vs prix
- Utilise **des segments (Slicer)** pour filtrer par nombre de pièces
- Utilise **des barres conditionnelles** pour voir les variations de prix

---

## Tu veux le fichier prêt ? 📥  
Je peux te donner :
- ✅ Le fichier **Excel avec les 50 lignes**
- ✅ Tous les graphiques prêts
- ✅ Des cases où tu peux **tester des prédictions**
