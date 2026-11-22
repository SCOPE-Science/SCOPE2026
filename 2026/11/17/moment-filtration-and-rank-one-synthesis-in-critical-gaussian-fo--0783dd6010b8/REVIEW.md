# Independent mathematical audit

## correctness

PASS

PASS: With e_k=z^k/sqrt(k!), each A_mj=I^(m+j)M_(z^m)D^j is exactly the 2m-forward weighted shift with coefficient P_m(k-j)/H_m(k) for k>=j, zero below j, P_m(X)=∏_(s=1)^m(X+s), H_m(k)=sqrt∏_(s=1)^(2m)(k+s). For finite c, the high tail polynomial Q_c(k)=Σ c_j P_m(k-j) has degree m-q iff q<=m first nonzero moment M_q, with leading (-1)^q binom(m,q)M_q. The nonzero shift singular values are decreasing rearrangements of |Q_c(k)|/H_m(k); this proves essential norm, n^-q, sharp Schatten membership and harmonic logarithmic endpoint. When all moments M_0..M_m vanish, C(t) has factor (1-t)^(m+1), and exact discrete rising-factorial identity, including low-index derivative cutoff, gives B_(m,h,m+1)=m! |e_(h+2m)><e_h|/H_m(h). Orthogonal rank-one supports yield exact finite rank, all singular values and rank = number nonzero polynomial-quotient coefficients. Independent exact integer check for all 1<=m<=7, 0<=h<=4, 0<=k<=19 verified the rank-one identity (700 cases); inspected full source CHECK.py covering wider m/h/q and moment/synthesis checks. Infinite statements rest on exact polynomial algebra rather than finite observations.

## originality

PASS

PASS, with explicit prior-coverage limitation: Dong–Hu supplies individual generalized integral weights and compactness; the earlier published polynomial Fock–Sobolev Weyl theorem gives broader leading singular-value and endpoint asymptotics for compact fixed-integration-order polynomial sums. By passing to a sufficiently high common integration order and commuting derivatives through z^m, it can also subsume the compact spectral-power portion here (up to finite rank). Those spectral asymptotics are not claimed as uniquely new in isolation. The substantive uncaptured result is the exact finite-difference endpoint where individually noncompact shifts combine to rank-one maps, the all-moment explicit polynomial-quotient finite-rank classification and full nonzero singular-value list, including low-degree cutoff and rank-one synthesis. The prior Weyl theorem treats nonzero negative-degree principal symbols and does not determine these exact finite-rank endpoints. No source read proves that classification.

## value

PASS

PASS: Classifying when finite combinations of individually noncompact natural Gaussian-Fock integration shifts jump through Schatten thresholds and finally become a specified finite-rank operator is a motivated operator-ideal/finite-rank synthesis result. The rank-one identity is exact for every m,h and yields a constructive basis of finite-rank elements in a natural span, not merely a numerical calculation or parameter rename. Previously known generic spectral asymptotics are explicitly separated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
