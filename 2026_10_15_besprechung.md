# Arbeitsaufträge
- Recherche betreiben
    - gibt es noch bei anderen Firmen PCB-Rogowski-Spulen
- gibt es wesentliche Unterschiede zwischen planaren und toroidalen Rogowski-Spulen?
    - also 'normale' (siehe Wikipedia) vs. auf PCB-designte Spulen mit Vias (siehe Paper von Maxi)
- muss der stromdurchflossene Leiter ringförmig umschlossen sein oder reicht es, das die Rogowski-Spule unter-/oberhalb des Leiters liegt?
- wie ist der Dynamikbereich der Rogowski-Spule?
    - ist er nach unten hin durch Rauschen überschattet?
    - ist er nach oben hin durch Sättigung beeinflusst?
- pragmatischer Teststand aufbauen (Kondensatorbank kurzschließen)

# Specs der Rogowski-Spule:
- di/dt = 10 A/us +- 10% (vielleicht auch 20%)
- u(t) = 0...5V
- Bandbreite: 1MHz
- Durchmesser: max. 4cm
- Recherche:
    - ist das in unserem Umfang möglich?
    - grobe Gleichungen
- Simulationen von H- und E-Feld-Ausbreitungen
- Konstruktionsoptimierung?
- PCB-Design
- wie sehr beeinflusst der aktuelle DC-Strom (0.5 - 10kA) die Sensitivität?