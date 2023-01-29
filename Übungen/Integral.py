import sympy as sym
# Aufgabe 4 Übungsblatt 10
a,b,x = sym.symbols('a,b,x')
# Integrieren
lsg = sym.solve(sym.integrate((x+1)**(1/3),(x,0,a)) - 5/2, a)
print(lsg)

# Aufgabe 5
fx = 12*(x**2) - 4*(x**3)
roots = sym.solve(fx)
print(roots)
lsg = sym.integrate(fx, (x, -1, 0)) + sym.integrate(fx, (x, 0, 3)) + abs(sym.integrate(fx, (x, 3, 5)))
print(lsg)

# hat nur nicht gestummen, weil nicht die signierte Fläche verlangt war, sondern der Gesamtinhalt