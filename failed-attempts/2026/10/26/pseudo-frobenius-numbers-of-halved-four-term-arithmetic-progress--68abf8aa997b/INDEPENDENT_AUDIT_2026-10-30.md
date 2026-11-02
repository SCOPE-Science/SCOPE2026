# Independent mathematical audit

## correctness

PASS

The quotient reduction T=S/2=<a,x,y>, with x=(a+d)/2 and y=(a+3d)/2=3x-a, follows by parity pairing of the two odd generators. The strictly increasing Apéry minima W(u)=floor(u/3)y+(u mod 3)x for 0<=u<a represent all residues since gcd(a,x)=1. The generator tests W(u)+x, W(u)+y and W(u)+a select the stated one or two maximal residue indices according to a mod 3. The resulting pseudo-Frobenius, Frobenius, and symmetry formulas are mathematically correct for odd coprime a>=5,d>=1. Independently implemented Dijkstra shortest-path Apéry enumeration and generator-based pseudo-Frobenius membership checks verified 817 admissible odd coprime parameter pairs a<82,d<52; finite checks support but do not establish the unrestricted proof.

## originality

FAIL

FAIL: Robles-Pérez and Rosales (2015), Theorem 2.8, Proposition 3.5 and Remark 3.8, already determine the exact pseudo-Frobenius pairs of <a,b,cb-δa> under the interval condition. For the audited T choose b=x, c=3, δ=1, cb−δa=y, with gcd(a,x)=gcd(x,y)=1, gcd(a,3)=1 when a mod 3 is 1 or 2, and x>=ceil(a/3). The paper explicitly extends its formula beyond ordered generators via Remark 3.8. Its two PF expressions Qy−x and (a−1)x−Qa−a (Q=floor((a−1)/3)) are algebraically identical to both published claimed cases R=1,2. The remaining R=0 branch is a standard symmetric gluing of 3<Q,x−Q> with the coprime generator x (a=3Q), not an independently identified novel exact invariant. Because two complete claimed cases are explicit corollaries of an older published stronger PF theorem and the last is routine standard structure, the final three-way classification fails the originality test as claimed.

## value

FAIL

FAIL as an asserted new mathematical finding: the natural quotient family is well-motivated, but the two non-symmetric PF cases simply specialize an existing complete three-generator PF formula, while the symmetric case is a standard two-generator gluing. Repackaging the covered arithmetic into a four-term quotient parameterization supplies no independently unknown sharp fact beyond the established results; correct calculations and reproducibility cannot alone rescue value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
