# Independent mathematical audit

## correctness

PASS

Starting from Wang--Ramdas equation (41), setting \(x=c^2\) yields an exact rational expression for \(G_n^{(c)2}\). Differentiating its logarithm gives sign proportional to \(n-x(t-1)\): the function increases to the unique optimizer \(x=n/(t-1)\) for \(t>1\), and increases to the limiting value one for \(t\le1\). Substitution gives the displayed envelope. The barrier equation, monotonicity in n, and Lambert-W limiting solution follow by direct algebra/asymptotics. The repository verifier numerically checks the algebra and representative barriers; it is not used as the proof.

## originality

FAIL

The fixed-time Wang--Ramdas martingale is exactly the normal-g-prior Bayes factor for a one-sample t statistic after the parameter conversion \(g_{\mathrm{reg}}=n/c^2\). The established local empirical-Bayes g-prior literature maximizes this marginal likelihood and gives \(\widehat g_{\mathrm{reg}}=\max\{F-1,0\}\). For the one-parameter mean test \(F=T^2\), this is exactly \(c_*^2=n/(T^2-1)\) when \(T^2>1\), with the boundary solution when \(T^2\le1\). Thus the central optimizer/envelope is a direct specialization of prior empirical-Bayes theory; the crossing barrier and Lambert-W limit are routine algebraic consequences of that covered envelope.

## value

FAIL

Once the prior local empirical-Bayes identity \(\hat g=F-1\) is recognized, the optimizer is substitution and the envelope/barrier are routine one-variable algebra. Recasting the same covered fixed-time Bayes-factor optimization as an oracle diagnostic for a sequential martingale does not add a new structural theorem, and the pointwise maximized process is not itself sequentially valid.

The dated certificate retains the supplied scientific assessment, sources and limitations.
