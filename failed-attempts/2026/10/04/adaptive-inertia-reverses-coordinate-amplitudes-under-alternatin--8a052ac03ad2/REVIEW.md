# Independent mathematical audit

## correctness

FAIL

The final claim audits the wrong Adai recurrence. The published Algorithm 2 sets \(\beta_{1,t}=\operatorname{Clip}(1-\beta_0\widehat v_t/\bar v_t,0,1-\epsilon)\), whereas the package uses the reciprocal ratio \(1-\beta_0\bar v_t/\widehat v_t\). This inversion reverses the intended parameterwise inertia dependence. For the package witness with squared-amplitude ratios \((1.6,0.4)\), \(\beta_0=0.1\), the actual source rule gives inertias \((0.84,0.96)\); the alternating-response amplitudes are approximately \((0.173913,0.020408)\) times the global step, so the larger raw-gradient coordinate remains larger rather than being reversed. Thus the advertised source-form Adai amplitude reversal is false.

## originality

FAIL

There is no valid original statement about the claimed source algorithm because the defining recurrence is miscopied. The algebra may describe a different reciprocal-ratio optimizer, but that is not Adai as published. A false attribution cannot be rescued as an original theorem about Adai, and no repaired claim was supplied in the package.

## value

FAIL

The claimed reversal is tied to a reciprocal-ratio update that is not the published Adai algorithm. Under the actual rule the displayed witness has the ordinary amplitude ordering, so no surviving correct Adai phenomenon remains to motivate publication. A separate study of the invented reciprocal-ratio method would be a different research question, not a repair of this claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
