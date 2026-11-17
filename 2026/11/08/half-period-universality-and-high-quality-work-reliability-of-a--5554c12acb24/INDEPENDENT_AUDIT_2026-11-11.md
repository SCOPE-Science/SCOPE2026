# Independent mathematical audit

## correctness

PASS

The pinned RESULT derives Gaussian x(h) with mean (a+f/k)(1-g(h)), and variance (Theta/k)(1-g(h)^2-(k/m)b(h)^2)=(2gamma Theta/m²)int_0^h b(s)^2 ds. Controller work is k a x(h); its mean is strictly convex in a and minimized at -f/(2k). K(h)=1-g(h) has unique first global maximum at h*=pi/omega; over extracting -f/k<a<0 it minimizes mean work. For fixed a, success=Phi((a+f/k)K/sqrt(Var x)). On first lobe b(s)=exp(-alpha s)sin(omega s)/omega is positive strictly log-concave; differentiation of F²/G with F=int b,G=int b² and H=2G-bF>0 proves success strictly grows until h*. For later h, K strictly below its maximum and G strictly larger, excluding other global maxima. At h* g=-q,b=0 gives exact mean, variance and Gaussian complement; expansion of q=exp(-gamma pi/(2m omega)) and Mills ratio yields provided exp[-f²m omega0/(2pi k Theta gamma)] prefactor. Direct numerical calculations for two independent parameter sets corroborate first-half-period score and variance. Strict control constraints are exactly two instantaneous jumps, NOT finite slew.

## originality

PASS

The originating Yao-Bao-Hou 2026 underdamped active-force paper states unrestricted minimum-mean-work and ideal work variance, not an inspected theorem on two-jump held-pulse mean-and-sign time optima or its pi²/8 ratio. Its original full text was not accessible on this run: arXiv and lawful OA attempts failed; authorized Oxford returned vpn_disconnected, so priority is qualified. Schuettler et al. 2025 treats overdamped moving traps, Gomez-Marin et al. 2008 passive ideal underdamped control. No indexed identical joint pulse theorem returned by Resultary. Unavailable original source is a significant unresolved historical risk, not a mathematical falsehood or automatic novelty failure.

## value

PASS

The proposed physical benchmark restricts an ideal distributional impulse controller to a single held trap displacement; finding one unique dwell time optimizing two distinct objectives (expected work and probability of extracting work) and exact exponentially rare failures is a motivated performance classification. The pulse still has instantaneous infinite-bandwidth jumps, so claims of implementable finite-slew control would be unsupported; they are not made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
