# Function-for-equations
# Zip function allows to itrate through x and y in parellel


#Spec Equation for july 17th

jul17_reflect = pd.read_csv("F:/Thesis/Thesis-Excel-Files/7-17/7-17-reflect.csv")
#data17 = pd.read_csv("F:/Thesis/Thesis-Excel-Files/7-17/7-17-surface.csv")

r596 = jul17_reflect['596.1']
r591 = jul17_reflect['591.8']

xp = Series.tolist(r596)
yp = Series.tolist(r591)

est_tp17 = []

def Esttp(x,y):
    for x, y in zip(xp, yp):
        score = 6.06 * math.log(x/y) + .14
        score = round(score, 3)
        est_tp17.append(score)

Esttp(xp, yp)
est_tp17

est_tp17 = pd.DataFrame(est_tp17)
est_tp17.to_csv("est_tp17.csv", sep = ",", index = False)
