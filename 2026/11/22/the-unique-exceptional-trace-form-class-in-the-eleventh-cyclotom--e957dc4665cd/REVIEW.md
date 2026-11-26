# Independent mathematical audit

## correctness

PASS

Chang's Corollary 4.9 applies to all totally positive weights in the real subfield and restricts a nonunit minimum to pi times a unit epsilon, of absolute norm 11. Proposition 5.2 gives the five simultaneous unit minima epsilon*pi/(1-zeta^k). Put A_k=(1-zeta^k)(1-zeta^(-k)) and b_j=sigma_j(a*epsilon*bar(epsilon)*A_1). The full-field trace of a real element is twice the quintic trace. The equal value equations are therefore M b=(sum b)1 with M_kj=sigma_j(1/A_k). I independently verified M1=5*1 and nonsingularity: writing w_r=r(11-r) for 0<=r<=10, the cyclic second differences of w give 1/A_k=-(1/22) sum_r w_r zeta^(kr) modulo Phi_11. The cyclotomic trace is 10 on 1 and -1 on every nontrivial 11th root. Cyclic convolution and half-trace give the stated rational Gram entries 11 on the diagonal and 3 or 4 off it, with determinant 75625. Replay: python3 /workspace/branches/audit-2/check_gram.py. This checks the trace sums and rank, not Chang's norm restriction. For a given positive sum, invertibility forces b=(sum b)/5 times 1; since the element represented by b has all five conjugates equal, it lies in Q with positive value c. This yields exactly a=c/(A_1*epsilon*bar(epsilon)). For sufficiency, Proposition 3.4 gives min 10 at a_0=1/A_1, attained by 1 and pi. Independently, writing y=x/pi=sum_j d_j*zeta^j with 11 coefficients, the trace of y*bar(y) is sum_{i<j}(d_i-d_j)^2. Since O/(pi)=F_11, y=z+m/pi for integral z and integer m modulo 11. For m=0 one can take integer coefficients; unless y=0, at least 10 pairs differ, so the trace is at least 10. For m!=0 the coefficients from 1/pi=(1/11)sum_{j=0}^{10}(10-j)*zeta^j have distinct residues modulo 1 after multiplication by m. Sorting the lifted coefficients gives spacing at least 1/11 and a lower bound sum_{d=1}^{10}(11-d)*d^2/121=10. The displayed coefficients for 1/pi realize equality, and integer coefficients of 1 do also. This proves the infinite reference bound independently of the finite Gram check. Multiplication by the inverse unit permutes O and yields min 10c with both epsilon and pi*epsilon attaining it. Thus the classification is one equivalence class, not one literal ray before unit twists. The uploaded checker was inspected, not executed.

## originality

PASS

Chang already proves the full-field weak reducibility, the norm-11 shape for any nonunit minimum, all five companion unit equalities and the reference example. The surviving novel step is weight rigidity: the five equalities have only the constant embedding vector at fixed scale. That identifies every positive weight admitting a nonunit minimum, up to rational and unit-norm actions. The inspected literature did not show this rigidity or the resulting classification; the historical perfect-form tables remain a specific unresolved source of implicit coverage.

## value

PASS

Weak unit reducibility leaves open where unit and nonunit minima can tie. Determining the complete exceptional locus in the five-embedding weight cone up to the natural actions answers that structural question, rather than merely locating one form. The independent finite rank calculation proves rigidity for every positive weight using the equality constraints, not just for samples or listed forms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
