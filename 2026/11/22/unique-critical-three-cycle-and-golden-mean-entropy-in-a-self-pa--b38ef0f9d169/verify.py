#!/usr/bin/env python3
"""Exact symbolic checks for a self-parameterized tent map.

Requires Python 3 and SymPy. These checks support, but do not replace,
the interval-expansion and Markov-entropy arguments in RESULT.md.
"""
import sympy as s

A = s.symbols('A', real=True)
x = s.symbols('x', real=True)
c = s.Rational(1, 2)
left = lambda z: s.expand((A + z / 4) * z)
right = lambda z: s.expand((A + z / 4) * (1 - z))
h = left(c)
l = s.factor(right(h))
assert s.factor(h - A / 2 - s.Rational(1, 16)) == 0
assert s.factor(l + (8 * A - 15) * (72 * A + 1) / 1024) == 0
q = s.factor(left(l) - c)
assert s.factor(q - (8*A - 7)*(72*A - 647)*(576*A**2 - 560*A - 463)/4194304) == 0
r = s.sqrt(337)
Astar = (35 + 4*r)/72
Cstar = 4*(Astar - s.Rational(37, 25))
assert s.simplify(Cstar - (100*r-1789)/450) == 0
lstar = s.simplify(l.subs(A, Astar))
hstar = s.simplify(h.subs(A, Astar))
assert s.simplify(lstar - (r-7)/36) == 0
assert s.simplify(hstar - (r+11)/36) == 0
assert s.simplify(hstar-lstar-c) == 0
assert s.simplify(q.subs(A,Astar)) == 0
assert 0 < Cstar < 1 and 0 < lstar < c < hstar < 1
# The required Markov endpoint images, all exactly in Q(sqrt(337)).
assert s.simplify(left(s.Integer(0)).subs(A,Astar)) == 0
assert s.simplify(left(lstar).subs(A,Astar)-c) == 0
assert s.simplify(left(c).subs(A,Astar)-hstar) == 0
assert s.simplify(right(c).subs(A,Astar)-hstar) == 0
assert s.simplify(right(hstar).subs(A,Astar)-lstar) == 0
assert s.simplify(right(s.Integer(1)).subs(A,Astar)) == 0
# The 4-cell adjacency graph; golden mean is its Perron root.
M = s.Matrix([[1,1,0,0],[0,0,1,0],[0,1,1,0],[1,0,0,0]])
t = s.symbols('t')
assert s.factor(M.charpoly(t).as_expr()) == t*(t-1)*(t*t-t-1)
core = s.Matrix([[0,1],[1,1]])
assert all(y > 0 for y in list(core**2))
print('PASS exact critical orbit, uniqueness polynomial, four-cell Markov matrix, core primitivity')
print('A* =', Astar, 'C* =', Cstar)
print('l =', lstar, 'h =', hstar)
print('Characteristic polynomial =', s.factor(M.charpoly(t).as_expr()))
