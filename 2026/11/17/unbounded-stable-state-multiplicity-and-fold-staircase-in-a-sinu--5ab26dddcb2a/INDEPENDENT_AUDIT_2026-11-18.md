# Independent mathematical audit

## correctness

PASS

The equilibrium equations give y=ax/m,z=Cx² and h_p(x)=Bx−Cx³+p sin x, B=r−a/m>0,C=a/(mc)>0. Cubic dominance bounds roots at T_p∼(p/C)^(1/3). Above R=√(B/C), each positive-sine lobe has h_p''=−6Cx−p sin x<0, negative endpoints and a single maximum; hence zero/one-double/two roots as p crosses p_j. Full activated lobes occupy asymptotic proportion T_p/(2π) of positive line and contribute two roots each, mirrored negatively. The fold minimizer satisfies tan(t_j−x_j)=P'(x_j)/P(x_j), giving x_j=t_j−3/t_j+O(t_j^-3), p_j=Ct_j³−(B+9C/2)t_j+O(t_j^-1). For the 3×3 Jacobian, A3=−mc h_p'(x), A2=a(1+c)+c−mr−mp cos x+(1+a/c)x² and A1=a+c+1. Left lobe roots have A3<0; right roots in every lobe ending at x≤(1−η)T_p satisfy cos x≤−κ_η, giving A2,A3,A1A2−A3>0 uniformly for large p. Letting η→0 matches lower and upper sink-count leading coefficients. Every stable root is a true 3D Hurwitz sink, not just a scalar root. Direct fresh high-p check for a=2,m=3,c=4,r=5,p=10^6 found 56 positive roots, 28 positive sinks, T_p=181.76; outer fold j=10 x=64.3558715 and p_j=44193.0183, matching asymptotic predictions 64.3560675 and 44193.1114. Finite diagnostics do not establish the asymptotics.

## originality

PASS

PASS on a model-specific quantitative complete equilibrium/sink growth law and infinite ordered fold mechanism. The exact sine-perturbed three-echelon model and moderate-p stable states were previously published; stability of every large lobe is new only if the full Hurwitz argument is not already implied by earlier literature.

## value

PASS

Infinite growth of simultaneously attracting stationary solutions in a natural fixed three-dimensional feedback ODE is nontrivial dynamical multistability. The exact sink coefficient and fold staircase separate scalar root creation from dynamical stability and provide a useful quantitative bifurcation boundary, even absent a global basin classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
