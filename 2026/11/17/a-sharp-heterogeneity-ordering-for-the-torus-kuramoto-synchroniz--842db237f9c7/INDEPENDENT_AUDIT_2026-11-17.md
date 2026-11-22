# Independent mathematical audit

## correctness

PASS

The conditional reduced ODE is specified, not an unproven claim about arbitrary microscopic networks. At a positive equilibrium, t=K prod x_i gives x_i=t/(t+d_i) and K=Phi_d(t)=prod(t+d_i)/t^{D-1}. The unique minimizer solves sum d_i/(t+d_i)=1, since its derivative changes from 1-D to 1 monotonically. The Jacobian is similar by diagonal x_i sqrt(d_i) to -diag(t+d_i)+sqrt(d) sqrt(d)^T; rank-one inertia proves upper branch attracting and lower branch one-unstable, with one zero eigenvalue at threshold. At t_c, envelope differentiation gives partial log K_c / partial d_i = q_i=1/(t_c+d_i), strictly antitone in d_i, proving Schur concavity. For X, implicit differentiation gives partial log X_c / partial d_i=q_i^2/R-q_i with R=sum d_k/(t+d_k)^2. The derivative difference equals (q_i-q_j)((q_i+q_j)/R-1); tR=sum x_k(1-x_k)<1 and t(q_i+q_j)=x_i+x_j>1 for D>=3 because sum x=D-1 and other D-2 entries <1. Thus this factor is positive and gives strict Schur concavity. At equal widths t=(D-1)m, K_c=m D^D/(D-1)^(D-1), X_c=((D-1)/D)^D; a sequence approaching (S,0,...,0) gives K_c down to S and X_c to zero. Tangent Hessian and sum x=D-1 yield the same relative -sum eps_i²/(2D²) in both observables. Independent numerical roots for d=(1,1,1), (.5,1,1.5), (.1,.1,2.8) give K=6.75,6.554959921,4.55625 and X=.296296,.287297,.175583; symmetric perturbation errors decrease approximately quartically. Analytic derivative inequalities, not these numerical instances, prove strict global majorization.

## originality

PASS

Novaes 2026 derives the precise reduced model, equilibrium scalar equation and unique saddle-node, including selected equal/partly equal dispersion examples; those are prior premises. The checked paper does not state the two global strict Schur orders for every positive rate vector or their identical quadratic penalty. General Schur–Ostrowski criterion is classical and credited; the new work is its nontrivial joint application to both K_c and X_c, especially the implicit derivative sign for X_c.

## value

PASS

Under a fixed frequency-width budget the theorem establishes a rigorous global prediction of how heterogeneity moves both the synchronization threshold and the coherence jump. Simultaneous strict orderings and sharp bounds for the exact bifurcation observables are natural parameters of an established mean-field model, despite relying on standard majorization calculus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
