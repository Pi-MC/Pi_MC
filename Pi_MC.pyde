#globale Definitionen
#Liste der Koordinaten
x = []
y = []

#Radius des Kreises
radius = 300

#Zähler für die Anzahl Punkte im Viertelkreis und im Viertelquadrat
counter_circle = 1
counter_square = 1

#Liste der Approximationen von Pi
pi_approx = []

#Anzahl angezeigter Punkte
points_shown = 0

#Maximale Anzahl berechneter Punkte
points_max = 1000

# Globale Variablen für Schieberegler von Simon Hefti
# movingMode (Boolean): True, wenn der Schieber (Kreis) in Bewegung ist, False wenn nicht
# pointerPos (Integer): Position des Pointers in Pixeln
# pointerVal (Float):   Eingestellter Wert (0 - 100)
movingMode = False
pointerPos = 0
pointerVal = 0.0




def setup(): #Initialisierung
    
    #globale Variablen
    global x
    global y
    global counter_circle
    global counter_square
    global pi_approx
    global points_max
    
    #Fenstergrösse und Hintergrundfarbe
    size(600,400)
    background(255,255,255)
    
    #Textfarbe und Textgrösse
    fill(0,0,0)
    textSize(20)
    
    frameRate(100) #Frequenz der draw-Funktion
    
    #Zufällige Koordinatenliste erstellen und Punkte zählen
    for i in range(0, points_max):
        x.append(int(random(0,300)))
        y.append(int(random(0,300)))
        
        #x^2 + y^2 <? radius^2
        if (pow(x[i], 2) + pow(y[i], 2)) < pow(radius, 2):
            counter_circle = counter_circle + 1
        else:
            #counter_circle = counter_circle + 1
            counter_square = counter_square + 1
            
        #Approximation von Pi
        pi_approx.append(round(4 * float(counter_circle) / float((counter_circle + counter_square)), 7)) #Conversion to float notwendig, da int / int wieder int gibt
    
    

def draw(): #Betriebsmodus
    
    #globale Koordinaten verwenden
    global x
    global y
    global radius
    global counter_circle
    global counter_square
    global pi_approx
    global pointerVal
    global points_shown
    global points_max
    
    #Hintergrund weiss, damit Animation funktioniert
    background(255,255,255)
    
    #Schieberegler zeichnen
    draw_ruler(50, 350, 500)
    
    #Schieberegler bestimmt, wieviele Punkte gezeigt werden
    points_shown = int(pointerVal * points_max)

    
    #Grundfigur
    noFill()
    square(10, 10, radius)
    arc(10, 310, 2 * radius, 2 * radius, -HALF_PI, 0)
    arc(10, 10, 2 * radius, 2 * radius, 0, HALF_PI)

    

    #Zufallspunkte zeichnen
    for i in range(0, points_shown):
        #x^2 + y^2 <? radius^2
        if (pow(x[i], 2) + pow(y[i], 2)) < pow(radius, 2):
            fill(255, 0, 0)
        else:
            fill(0, 255, 0)
        ellipse(x[i] + 10, -y[i] + 310, 5, 5)
    fill(0)
        
    #Pi Texte
    #text("Pi = 4*" + str(counter_circle) + "/" + str(counter_square) + str(pi_approx[points_shown-1]), 400, 100)
    text("Pi = " + str(pi_approx[points_shown-1]), 400, 100)
    text("Pi = 3.1415926", 400, 160)
    
    


'''
' Schieberegler
' Simon Hefti, Okt. 2020
'''
# Funktion: Schieberegler generieren
# objX:      X-Position des Reglers
# objY:      Y-Position des Reglers
# objLength: Länge des Reglers
def draw_ruler(objX, objY, objLength):
    global movingMode
    global pointerPos
    global pointerVal
    
    # Schieber einstellen
    pointerRadius = 24
    if pointerPos == 0:
        pointerPos = objX
    
    # Linie zeichnen
    #fill(0)
    #strokeWeight(6)
    line(objX, objY, objX + objLength, objY)
    #fill(0)
    #strokeWeight(2)
    
    # Überprüfen ob Schieber angeklickt worden ist --> Bewegungsmodus aktivieren
    if mouseX > pointerPos - pointerRadius and mouseX < pointerPos + pointerRadius and mouseY > objY - pointerRadius and mouseY < objY + pointerRadius and mousePressed == True:
        movingMode = True
    
    # Wenn keine Maustaste gedrückt ist --> Bewegungsmodus deaktivieren
    if mousePressed == False:
        movingMode = False
        cursor(ARROW)
    
    # Bei aktiviertem Bewegungsmodus
    if movingMode == True:
        cursor(HAND)
        
        # Schieber der Line entlang bewegen
        if mouseX > objX and mouseX < objX + objLength:
            pointerPos = mouseX
        
        # Wenn Maus ausserhalb der Linie, Schieber am Start oder Ende fixieren
        else:
            if mouseX < objX:
                pointerPos = objX
            if mouseX > objX:
                pointerPos = objX + objLength

    # Schieber zeichnen            
    circle(pointerPos, objY, pointerRadius)
    
    # Eingestellter Wert anhand der Schieberposition ermitteln (modifiziert)
    pointerVal =  (pointerPos - objX) / float(objLength)
            
