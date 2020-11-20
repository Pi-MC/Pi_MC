#globale Definitionen
#Liste der Koordinaten
x = []
y = []

#Radius des Kreises
radius = 300

#Anzahl Punkte im Viertelkreis und im Viertelquadrat
counter_circle = 1
counter_square = 1

#Approximation von Pi
pi_approx = -1
 

def setup(): #Initialisierung
    
    #globale Variablen
    global x
    global y
    global counter_circle
    global counter_square
    global  pi_approx
    
    #Fenstergrösse und Hintergrundfarbe
    size(600,400)
    background(255,255,255)
    
    #Textfarbe und Textgrösse
    fill(0,0,0)
    textSize(20)
    
    frameRate(100) #Frequenz der draw-Funktion
    
    
    #Zufällige Koordinatenliste erstellen und Punkte zählen
    for i in range(0, 20):
        x.append(int(random(10,310)))
        y.append(int(random(10,310)))
        
        #x^2 + y^2 <? radius^2
        if (pow(x[i], 2) + pow(y[i], 2)) < pow(radius, 2):
            counter_circle = counter_circle + 1
        else:
            counter_circle = counter_circle + 1
            counter_square = counter_square + 1
            
    #Approximation von Pi
    pi_approx = round(4 * float(counter_circle) / float((counter_circle + counter_square)), 7) #Conversion to float notwendig, da int / int wieder int gibt
    
    

def draw(): #Betriebsmodus
    
    #globale Koordinaten verwenden
    global x
    global y
    global radius
    global counter_circle
    global counter_square
    global pi_approx
    
    #Hintergrund weiss, damit Animation funktioniert
    background(255,255,255)
    
    #Grundfigur
    noFill()
    square(10, 10, radius)
    arc(10, 310, 2 * radius, 2 * radius, -HALF_PI, 0)
    

    #Zufallspunkte zeichnen
    for i in range(0, 20):
        ellipse(x[i], y[i], 5, 5)

        
    #Pi Texte
    text("Pi = " + str(pi_approx), 400, 300)
    text("Pi = 3.1415926", 400, 360)
