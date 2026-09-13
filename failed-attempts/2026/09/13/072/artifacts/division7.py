"""Order-7 point via division polynomials on monic model (Y')^2=(X')^3+a2(X')^2+a4 X'+a6, lam=2."""
import numpy as np
a2,a4,a6 = -12.0, 37.333333333333336, -29.037037037037038
b2=4*a2; b4=2*a4; b6=4*a6; b8=a2*a6-a4**2
print("b2,b4,b6,b8=",b2,b4,b6,b8)
# psi recurrence: psi0=0,psi1=1,psi2=2Y,psi3=3x^4+b2 x^3+3b4 x^2+3b6 x+b8,
# psi4=psi2*(2x^6+b2 x^5+5b4 x^4+10b6 x^3+10b8 x^2+(b2b8-b4b6)x+(b4b8-2b6^2))/2 ... use standard polys in x only via phi/omega? Simpler: use Sage formulas for psi_n^2 / psi_n directly with numpy polys.
import numpy.polynomial.polynomial as P
def pmul(f,g): return np.convolve(f,g)
def padd(f,g):
    n=max(len(f),len(g)); o=np.zeros(n); o[:len(f)]+=f; o[:len(g)]+=g; return o
def psub(f,g):
    n=max(len(f),len(g)); o=np.zeros(n); o[:len(f)]+=f; o[:len(g)]-=g; return o
x=np.array([0.,1.])  # x
# psi3, psi4/psi2 etc. Use recurrence for E_n = psi_n^2 (polys in x after eliminating y^2=f):
f = padd(padd(padd(np.array([a6,a4,1.0])*1, np.array([0,0,0,a2])),np.array([0.0])),np.array([0.0]))  # a6+a4 x+x^3+a2 x^2
print("f=",f)
psi3 = padd(padd(padd(padd(3*x**4 if False else np.array([0,0,0,0,3.0]), b2*np.array([0,0,0,1.0])), 3*b4*np.array([0,0,1.0])), 3*b6*np.array([0,1.0])), np.array([b8]))
print("psi3 deg:",len(psi3)-1)
# psi5,psi7 via standard recurrence (Washington): psi_{m+2} psi_m^3 ... use doubling formulas:
# psi_{2n+1} = psi_{n+2}^3 psi_{n-1} - psi_{n-1}^3 psi_{n+2} ... careful: psi_{2n+1}=psi_{n+2}psi_n^3 - psi_{n-1}psi_{n+1}^3 (up to y factors absorbed in E_n).
# Work with E_n = psi_n^2 for odd n (poly), O_n = psi_n^2/(y^2)=psi_n^2/f for even n (poly). Recurrences (Washington Thm):
# E_{2n+1} = E_{n+2} E_n^3 - E_{n-1} E_{n+1}^3  (n even? general with correct E/O mix). Full mixed rules:
# psi_{2n+1} = psi_{n+2} psi_n^3 - psi_{n-1} psi_{n+1}^3.
# psi_{2n} = (psi_{n+2} psi_{n-1}^2 - psi_{n-2} psi_{n+1}^2) psi_n / (2y).
# In E/O: E_{2n+1} = G(n+2)G(n)^3 - G(n-1)G(n+1)^3 where G(k)=E_k (k odd), G(k)=f*O_k (k even).
# and f*O_{2n} ... = (G(n+2)G(n-1)^2 - G(n-2)G(n+1)^2)^2 G(n) /4 ... let H_n = psi_n^2 as rational: H_n = E_n (n odd), f O_n (n even).
H={0:np.array([0.]),1:np.array([1.]),3:psi3}
# O_2 = 4 (since psi_2^2=4y^2=4f) -> H_2 = 4f
H[2]=4*f
def G(k): return H[k]
for n in [1,2,3]:
    # compute E/O for 2n+1 and 2n+2? need H_4 first: from formula psi4 = psi2*(x^6+...)/2 -> H4 = H2 * S^2 /4 where S = poly.
    pass
S = None
# S for psi4: 2x^6+b2 x^5+5 b4 x^4+10 b6 x^3+10 b8 x^2+(b2 b8-b4 b6)x+(b4 b8-2 b6^2), then psi4=psi2*S/2 -> H4 = H2*S^2/4
S = padd(padd(padd(padd(padd(padd(2*np.array([0,0,0,0,0,0,1.0]), b2*np.array([0,0,0,0,0,1.0])), 5*b4*np.array([0,0,0,0,1.0])), 10*b6*np.array([0,0,0,1.0])), 10*b8*np.array([0,0,1.0])), (b2*b8-b4*b6)*np.array([0,1.0])), np.array([b4*b8-2*b6**2]))
H[4]=pmul(H[2],pmul(S,S))/4.0
print("H4 deg:",len(H[4])-1)
# H5 (n=2): H5 = H4*H2^3 - H1*H3^3
H[5]=psub(pmul(H[4],pmul(H[2],pmul(H[2],H[2]))), pmul(H[1],pmul(H[3],pmul(H[3],H[3]))))
print("H5 deg:",len(H[5])-1, "(expect 12)")
# H6: psi6 = psi3*(... )*psi2... use H6 = H3 * T^2 /4? psi6 = psi3*(x^... )*psi2/(2y)... Actually psi_{2n} formula with n=3: psi6 = (H-comb)*psi3/(2y) -> H6 = COMB^2 * H3 / (4f), COMB = G5 G1^2 - G1 G4^2? G5=H5,G1=H1,G4=H4: COMB = H5*H1 - H1*H4 = H1*(H5-H4)?? indices: G(n+2)G(n-1)^2 - G(n-2)G(n+1)^2, n=3: G5 G2^2 - G1 G4^2.
COMB = psub(pmul(H[5],pmul(H[2],H[2])), pmul(H[1],pmul(H[4],H[4])))
H[6] = pmul(pmul(COMB,COMB),H[3])/(4.0*f[0]*0+4)  # polynomial division by 4f needed!
# proper poly long division by f
q,r = np.polydiv(np.poly1d(H[6]*4/4),np.poly1d(f[::-1])); 
print("sanity H6 pre-div deg:",len(H[6])-1)
num = pmul(pmul(COMB,COMB),H[3])
q,r = np.polydiv(np.poly1d(num[::-1]), np.poly1d((4*f)[::-1]))
print("rem deg:", (r.order if hasattr(r,'order') else '?'), r)
H[6]=q.coeffs[::-1]
print("H6 deg:",len(H[6])-1,"(expect 17)")
# H7 (n=3): H7 = H5*H3^3 - H2*H4^3
H[7]=psub(pmul(H[5],pmul(pmul(H[3],H[3]),H[3])), pmul(H[2],pmul(pmul(H[4],H[4]),H[4])))
print("H7 deg:",len(H[7])-1,"(expect 24)")
rts=np.roots(np.poly1d(H[7][::-1]))
rts=[z for z in rts if abs(z.imag)<1 or True]
print("H7 roots (X'):",np.sort_complex(rts))
np.save("output/artifacts/H7roots.npy", np.array(rts))
