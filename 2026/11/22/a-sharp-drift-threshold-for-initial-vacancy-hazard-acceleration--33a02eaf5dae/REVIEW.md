# Independent mathematical audit

## correctness

PASS

On the homogeneous ring the 10 and 01 bond counts agree, giving equal incoming/outgoing rates and hence the uniform stationary law in the fixed-charge sector. Stationary flux into the vacant sector has weight a=pX+qY, with X,Y the clockwise and counterclockwise occupations next to the probe; killing has rate c=qX+pY, a different quantity unless rates agree. Palm entrance is the mixture of uniform conditional laws given X=1 or Y=1, with weights p/(p+q), q/(p+q). For the subgenerator Q keeping the full negative diagonal, Q1=-c and differentiating survival gives h(0)=E_Palm c and h'(0)=h(0)^2+E_Palm Qc. Independently evaluating by this mixture gives E_Palm c=[2pq+(p²+q²)alpha]/(p+q), E_Palm c²=pq+(p²+pq+q²)alpha, and E_Palm G_int c=pq(alpha-1)+(p-q)²(alpha-beta). Here the conditional first and second moments on distinct remaining sites are alpha and beta; the two second-nearest sites coincide at L=4 but are never multiplied together. Subtracting c² gives the claimed slope. Putting m=L-2, s=p²+q² and u=pq, multiplying the slope by (p+q)² gives [alpha(1-alpha)/(m-1)](s²-4mu²)-2(1-alpha)us. This yields exactly the sign polynomial in z=s/u, with negative F(2), negative constant term and exactly one positive root; monotonicity of r+1/r for r>1 gives the unique positive-magnitude threshold and reciprocal. N=1 leaves a negative term; N=L-1 leaves a single vacancy state with exponential survival. For N/L→rho in (0,1), the positive root and r* are both asymptotic to 2L/rho. As a rational check, L=4,N=2,p=6,q=1 gives h(0)=61/14 and h'(0)=193/196. For reversibility, write A=-Q in the stationary weighted inner product; detailed balance gives entrance density proportional to A1 and survival spectral weights proportional to lambda times the squared spectral coefficients of 1. Thus the age derivative of the reversible hazard is minus the tilted variance. This proof is local in age for the driven model and does not infer reversibility from a negative slope. Inspected VERIFICATION.md and check_hazard.py; did not execute the frozen checker.

## originality

PASS

The exact result that survives comparison is the sign threshold and density scaling for the departure-Palm empty spell on a finite homogeneous ASEP ring. The reversible spectral-mixture mechanism is standard; a related Resultary result establishes it for a different time-stationary observable. Neither fixed-site occupation-time/correlation work as inspected nor stationary tagged-branch waiting laws supply the finite-sector derivative and threshold. This is a best-of-knowledge decision on the available statements; access to an occupation-time lead remained unresolved.

## value

PASS

This quantifies when a single site's vacancy-age record can witness failure of detailed balance without measuring any spatial current. The exact sign boundary is not an arbitrarily selected rate example: it separates all biases in each interior fixed-charge sector, distinguishes both boundary sectors, and requires bias of order L at positive limiting density. It is a one-sided theoretical diagnostic and does not claim full-age monotonicity, necessity, or finite-sample detectability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
