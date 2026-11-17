# Independent mathematical audit

## correctness

PASS

For the metric multigraph with r>=3 unit parallel edges plus a pendant h, centered resistance Green representation gives Q(x)=F(x)/(r+h)-J/[2(r+h)^2]. On each parallel edge F=F0+(h/r)t+k t(1-t) with k=r-2+(r-1)h/r>0, and its unique maximum occurs at x=(r-2+h)/(2k). On the pendant F=F0+z²+(r-h)z is convex and its tip exceeds the junction by rh. Direct integration of profiles gives J=[r²+(r+2)h+3rh²+h³]/3. The difference of two candidate maxima has exactly one positive zero; solving 4rhk=(r-2+h)^2 gives the displayed h_r, 0<h_r<1 and limit 1/4. Scalar multiples of centered representers are the complete equality functions. My independent sympy checks at r=3,4,11 verified the radical identity and candidate-value equality; the broad resistance envelope independently yields the same curvature k.

## originality

PASS

Baker–Faber supplies resistance curvature, while a later published general metric-graph quadratic envelope provides an algorithm for all graphs; neither states the displayed r-dependent pendant switching threshold or extremizer locations without specializing and optimizing. A related loop-bouquet with pendant has a different topology and threshold; no earlier matching full classification was located. The broad envelope publication commit (Nov9 01:09:49Z) is later than the assigned source commit (Nov8 23:31:40Z), but chronology is not treated as guaranteed priority.

## value

PASS

The exact norm and discontinuous localization transition are a motivated network geometry phenomenon: grafting a leaf changes where the largest mean-zero Sobolev evaluations concentrate. The radical boundary, all equality points, and nontrivial r→∞ limit are useful exact information for this natural multigraph, not a guessed arithmetic slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
