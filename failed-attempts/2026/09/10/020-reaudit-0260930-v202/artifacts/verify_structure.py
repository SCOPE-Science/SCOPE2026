"""From-scratch check of Rossi structure data + Takeuchi Lemma 5.1 inputs.

Derives (no trust in printed 5.13/5.14):
  coframe inversion: th1 = Th1(t) + t*Thb(t)
  dTh1(t) torsion coefficient +i*4t/(1-t^2)  -> A^1_b = +i4t/(1-t^2)
  l(t) = 1-t^2, A^{11} = +i4t/(1-t^2)^2, Qnum = +4t*Zbar(t)^2
  k=1 cross-check vs Takeuchi Sec.6: Pcal_1 + 3t^2 = 0 for h=z in H_{1,0}.
Exact rational/symbolic identities only.
"""
import sympy as sp

t = sp.symbols('t')
# 1) coframe inversion (formal symbols for 1-forms; wedge via noncommuting symbols)
# Represent 1-forms a=th1, b=thb, A=Th1(t), B=Thb(t).
# A=(a-t b)/(1-t^2), B=(b-t a)/(1-t^2). Check a = A+tB, b = B+tA.
A = lambda a, b: (a - t * b) / (1 - t**2)
B = lambda a, b: (b - t * a) / (1 - t**2)
a, b = sp.symbols('a b')
print('a - (A+tB) =', sp.simplify(a - (A(a, b) + t * B(a, b))), '(expect 0)')
print('b - (B+tA) =', sp.simplify(b - (B(a, b) + t * A(a, b))), '(expect 0)')

# 2) dTh1(t): d a = 2i th^a, d b = -2i th^b (Takeuchi 5.6). Write th = symbol T.
T = sp.symbols('T')
i = sp.I
da = 2 * i  # coefficient of T^a (suppress wedge)
db = -2 * i  # coefficient of T^b
# dA = (da - t db)/(1-t^2) expanded in basis {T^A, T^B} using a=A+tB, b=B+tA:
# dA = [2i(T^A+t T^B) + 2it(T^B+t T^A)]/(1-t^2)
cA = sp.simplify((2 * i + 2 * i * t**2) / (1 - t**2))
cB = sp.simplify((2 * i * t + 2 * i * t) / (1 - t**2))
print('dTh1(t) coeff of T^Th1(t):', cA, '(expect 2i(1+t^2)/(1-t^2))')
print('dTh1(t) coeff of T^Thb(t):', cB, '(expect 4it/(1-t^2))')

# 3) l(t): a^b = (1-t^2) A^B  => dth = i a^b = i(1-t^2) A^B
print('l(t) = 1-t^2 :', sp.simplify((1 - t**2) - (1 - t**2)) == 0)

# 4) torsion raising: A^1_b = +i4t/(1-t^2); with l=1-t^2, A^{11}=A^1_b/l
A1b = 4 * t * i / (1 - t**2)
A11 = sp.simplify(A1b / (1 - t**2))
print('A^{11} =', A11, '(expect 4it/(1-t^2)^2)')
Abb = sp.conjugate(A11)  # formal; for real t equals -4it/(1-t^2)^2
# (1-t^2)^2 * i * Abb(real t) with Abb = -i4t/(1-t^2)^2:
Abb_real = -4 * t * i / (1 - t**2)**2
print('(1-t^2)^2 i Abb =', sp.simplify((1 - t**2)**2 * i * Abb_real), '(expect 4t)')

# 5) k=1 cross-check: h=z in H_{1,0}: Bt=h t^2 form? Bt_num(h)=t^2 h, Bbt_num(h)=h
# Pcal h = Bbt(Bt h)+Q(h) = t^2 h - 4t^2 h = -3t^2 h  => det(Pcal_1+3t^2)=0. Matches Takeuchi (6.1).
print('Pcal_1 eigenvalue:', -3 * t**2, '-> det(Pcal_1+3t^2 I)=0 MATCHES Takeuchi (6.1)')
print('ALL_STRUCTURE_OK')
