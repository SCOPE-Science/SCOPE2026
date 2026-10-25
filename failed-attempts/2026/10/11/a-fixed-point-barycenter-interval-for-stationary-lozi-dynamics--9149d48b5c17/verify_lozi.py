from sympy import symbols, simplify
a,b,pp,pm=symbols("a b pp pm", positive=True)
A=a+1-b
B=a+b-1
m=pp-pm
budget=A*pp+B*pm
xp=1/A
xm=-1/B
# Assuming budget=1, verify the two defect identities algebraically after substituting 1=A*pp+B*pm.
expr1=simplify((xp-m) - (2*a/A)*pm)
expr1_reduced=simplify(expr1.subs(pp,(1-B*pm)/A))
expr2=simplify((m-xm) - (2*a/B)*pp)
expr2_reduced=simplify(expr2.subs(pm,(1-A*pp)/B))
assert expr1_reduced==0
assert expr2_reduced==0
# Verify A+B=2a, the coefficient identity behind the budget decomposition.
assert simplify(A+B-2*a)==0
print("LOZI_IDENTITY_OK")
