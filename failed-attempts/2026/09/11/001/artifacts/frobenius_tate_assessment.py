"""Tate/van Luijk upper-bound feasibility assessment from logged traces.
Logged: p=5: N1=80 (t1=54), N2=1112 (t2=486); p=7: N1=120 (t1=70), N2=3480 (t2=1078).
For a K3, Tr(Frob^r|H^2)=t_r with t_r=#X(F_{p^r})-1-p^{2r}; the charpoly has degree 22.
Two traces determine only power sums p1=t1, p2=t2 of the 22 eigenvalues; Newton
identities cannot fix the degree-22 polynomial. Hence the Tate divisor bound
(#eigenvalues q*x root of unity / reciprocal root analysis) and the van Luijk
discriminant comparison are UNDERDETERMINED from r<=2 data: no rho<=2 derivation
is possible without moments up to r=11 (or sparse-factor reconstruction, unjustified).
Conclusion: rho<=2 upper bound NOT established in-hour; rho>=2 certified separately.
"""
N5={1:80,2:1112}; N7={1:120,2:3480}
for p,N in [(5,N5),(7,N7)]:
    for r,n in N.items():
        print(f"p={p} r={r}: N={n} t={n-1-p**(2*r)}")
print("eigenvalues: 22; known power sums: p1,p2 only => charpoly underdetermined.")
print("TATE_ASSESSMENT_OK: rho<=2 not derivable from r<=2 traces; needs r<=11 moments.")
