# Independent mathematical audit

## correctness

PASS

An independent all-direction linearization confirms the coefficient. At step j the centered vertices are λv_i, λ=(−1/3)^j, with v_i·v_i=3/4, v_i·v_l=−1/4 for i≠l, and Σv_iv_iᵀ=I. Write their first variation as D_i=aP+b(v_i·P)v_i. To propagate it, write D_i=T+λFv_i, where T=(a+b/4)P and λF=bΣ(v_l·P)v_lv_lᵀ; to first order the transformed face normal is v_i−Fᵀv_i and the offset is −λ/4+v_i·T. Differentiation of the perpendicular foot gives a′=1−b/12, b′=(4/3)(a−1)+2b/9, so from (0,0) one obtains b at steps 1–4 equal to −4/3, −8/27, 20/243, 112/2187. At step four λ=1/81; the derivative of each normalized edge square is (112/27)(v_i+v_l)·P, since the mean variation vanishes. The six pair sums are exactly the signed Cartesian unit vectors. This proves the all-direction norm and the positive lower bound away from zero locally. The foot map is smooth near these nondegenerate centered iterates.

## originality

FAIL

The distinct indexed regular-simplex result gives the exact axial Jacobian, not just a non-return statement. Its d=3, N=4 instance yields the claimed numerical coefficient by one matrix power and the conversion to the given edge normalization. Routine tetrahedral equivariance then forces that same norm ratio in every direction. Thus the claimed sharpening is mechanically covered; this is a statement-level implication, not a finding of historical order between same-day records.

## value

FAIL

The problem and norm are natural and the coefficient is correct, but taking a fixed power of the available exact axial Jacobian and applying ordinary regular-tetrahedron symmetry leaves no distinct nonroutine exact invariant as frozen. The finding does not add a global or nonlinear rigidity bound beyond that consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
