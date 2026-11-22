# Independent mathematical audit

## correctness

PASS

For a,b>0 and |kappa|<2sqrt(ab), Q=-(B+B^T)>0 has stationary covariance I. Direct exponential C=e^{tB}=[[u,kappa r],[0,v]] has singular values s_±<1 since I-CC^T=integral_0^t e^{sB}Qe^{sB^T}ds>0. The exact inverse/ordinary OU unitary conjugacy (Bruno et al Lemma 4.2) and symmetric Fock second quantization give singular values e^{-(a+b)t}s_+^j s_-^k, hence S_p^p=e^{-p(a+b)t}/[(1-s_+^p)(1-s_-^p)] for all real p>0 by summing positive geometric series. All eigenvalues depend only on diagonal u,v, while operator norm is vacuum e^{-(a+b)t}. With s_+s_-=uv fixed, larger |kappa| increases s_+/s_- and strictly decreases the product denominator for every p>0. HS denominator det(I-CC^T)=(1-u²)(1-v²)-kappa²r². At endpoint kappa*=2sqrt(ab), Q=qq^T, det[q,Bq]=-2sqrt(ab)(a+b) !=0, so Gramian remains positive for t>0; its determinant has leading det[q,Bq]^2 t^4/12=ab(a+b)^2 t^4/3. Add delta r(t)² with delta=4ab-kappa² and delta/t²->xi to obtain t^4 HS²->1/(xi+ab(a+b)^2/3), versus t² HS²->1/delta for fixed interior. Independent sympy check confirms bracket and signs. Product Schatten formula as general mathematics is known, and rank-one Gramian exponent is not new by itself.

## originality

PASS

Best-of-knowledge originality restricted to strict shear optimization in fixed-spectrum planar OU and the explicit simultaneous ellipticity/time crossover. The general second quantization Schatten product (Araki et al 1995) and inverse OU intertwining (Bruno et al 2026) are openly preexisting; a separate Resultary Kalman-grading result gives general rank-degenerate exponents in dimension at least 3 and does not directly imply the fixed-spectrum two-parameter extremal family.

## value

PASS

The same stable eigenvalues and trace mask arbitrarily enhanced short-time Hilbert-Schmidt growth near degenerating diffusion. Exact fixed-spectrum nonnormality discrimination across all Schatten orders and the t²-to-t⁴ boundary window are meaningful quantitative operator diagnostics, beyond re-stating an old Fock product formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
