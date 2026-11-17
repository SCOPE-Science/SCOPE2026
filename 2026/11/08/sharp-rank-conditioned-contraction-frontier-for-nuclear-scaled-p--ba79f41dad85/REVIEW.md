# Independent mathematical audit

## correctness

PASS

With G=U diag(s)V^T, S=sum s_j, D=sum s_j^2 u_j^T H^-1u_j=2f, and t=tr(U^THU), direct expansion yields ratio 1-alpha(2-alpha*t)S^2/D. Because alpha<2/T_r, t<=T_r makes the progress term positive. For a marked column u_k, the matrix of squared orthogonal-completion coordinates is doubly stochastic, hence a linear functional alpha*t+J u_k^TH^-1 u_k is maximized at a permutation. The marked eigenvalue i and r-1 remaining largest eigenvalues produce alpha*T_{r,i}+J/lambda_i<=2 for J=min_i lambda_i(2-alpha T_{r,i}). Choosing maximum H^-1 frame diagonal and using D<=dmax sum s_j^2<=dmax S^2 implies the exact q_r. A rank-r eigenframe with singular values 1,eps,...,eps reaches each extremal branch in the limit, and positive eps ensures strict nonattainment for r>1. Rank 1 is attained. q_{r+1}>q_r at common allowable steps; positivity of all branch second derivatives gives strict convexity/unique interior minimizer; top-r eigenframe proves exact alpha=2/T_r threshold; right-factor support proves rank nonincrease. Independent rational permutation calculations establish the H=(1,10,11),r=2,alpha=2/25 value 573/625 and alpha=1/12 optimum 11/12, and check other rational spectra. These are checks, not a replacement for the Birkhoff argument.

## originality

PASS

The central surviving claim is the exact arbitrary-spectrum intermediate gradient rank 1<r<d fixed-step envelope, with coupled marked eigenvalue assignment, nonattainment, rank-activation penalty and tuning. Rank-one ordinary gradient descent, full-row/full-rank case, rank monotonicity, one-step loss identity and exact descent threshold are already prior. The primary Jawanpuria paper was read in full rendered HTML, including Appendix C; a highly relevant Shulgin paper was identified from its abstract/research review but its complete text could not be retrieved, leaving material historical priority risk. No matching intermediate-rank formula found by semantic published records; best-of-knowledge O not global certification.

## value

PASS

The naturally motivated optimization problem corrects a looseness in prior quadratic Muon bounds: separately optimizing minimum curvature and trace ignores their coupling inside a rank-limited singular subspace. The exact marked-index formula, sharp nonattainment, strict activation penalty and computable fixed-rank optimal step provide quantitative anisotropic information not given by elementary unconditioned trace bounds; no large downstream theorem is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
