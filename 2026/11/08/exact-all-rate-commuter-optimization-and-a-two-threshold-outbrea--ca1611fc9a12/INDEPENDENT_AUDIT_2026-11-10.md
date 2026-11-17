# Independent mathematical audit

## correctness

PASS

The model fixes 0<R1<R2, N_i>0, positive rates and stationary demographic balances. P1=N1-e1x+e2y and P2=N2+e1x-e2y remain positive, S=k1x+k2y, u=S/P1,v=S/P2. The exact 2x2 matrix is Q=[[R1(1-u),R2v],[R1u,R2(1-v)]], whose column sums are R1,R2; Perron L lies between them for S>0. F(L)=(L-R1)(L-R2)+R1u(L-R2)+R2v(L-R1) has F_L>0. The identity R2(L-R1)v=(R2-L)[L-R1+R1u] and uv_y-vu_y>0 force F_y>0,L_y<0. At any L_x=0, v_x>0, u_xx>0,v_xx<0 force F_xx<0, so every stationary point is a strict nondegenerate minimum and there can be at most one. Continuity handles (0,0). For stated rational witness, independently expanded det(I-Q)=(4x^2-7x+1)/[40(x-5)(x+1)] and exact signs at x=0,3/4,1,2. Roots give the claimed strict subcritical interval. The derivative argument covers all allowed positive rates; numerical examples alone do not.

## originality

PASS

Rapaport–Mimouni (2022/23) derive this exact next-generation model, prove preliminary qualitative commuter effects and a trichotomy in the fast-commuting approximation (gamma dropped in residence factors); exact transfer only when gamma is sufficiently small. The submitted proof removes any fast/slow-rate assumption, establishes global one-valley uniqueness and an exact algebraic intervention interval with recovery as large as travel rates. Targeted same-model prior result/search has not revealed these quantitative all-rate conclusions; this distinction, not general commuter benefits, earns best-of-knowledge originality.

## value

PASS

Exact optimal commuter participation and two distinct invasion-threshold crossings are motivated, mathematically nontrivial properties of a published epidemic model. Removing the asymptotic assumption is substantively useful because policy rates need not be scale separated; uniqueness and a rational two-threshold witness give reliable sharp boundaries. Does not assert epidemic final size or neutral-threshold behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
