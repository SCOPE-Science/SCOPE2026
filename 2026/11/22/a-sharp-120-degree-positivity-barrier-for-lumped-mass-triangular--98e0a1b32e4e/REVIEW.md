# Independent mathematical audit

## correctness

PASS

The area is h and each lumped mass is h/3, so with b=h^2 the normalized stiffness is 3/(4b) times the symmetric matrix with rows (1+b,1-b,-2), (1-b,1+b,-2), (-2,-2,4). Its eigenvectors (1,1,1),(1,-1,0),(1,1,-2) give eigenvalues 0,3/2,9/(2b). For the resolvent R(u)=(I+uH)^(-1), put x=3u/(2b). Direct evaluation gives R_12=x(2bx+b-1)/(2(1+bx)(1+3x)), R_13=R_23=x/(1+3x), and R_33=(1+x)/(1+3x). All resolvent diagonals are positive, proving backward Euler's positive-step threshold. For CN use 2R(tau/2)-I. Its off-diagonal lower bound is x>0 with x>=(1-b)/(2b), and the apex diagonal forces x<=1. On that entire range the base diagonals are positive: they equal (1+2x-bx^2)/((1+bx)(1+3x)). This gives the closed interval in physical time, nonempty for b>=1/3, and the stated critical matrix. Zero time is the identity in all cases. In the exponential, only the base transfer can change sign; its numerator is 2+exp(-3z)-3exp(-bz) with z=3tau/(2b). Its derivative is negative before log(1/b)/(3-b), positive after, and the numerator goes from 0 to negative values and then to limit 2. There is exactly one positive recovery root. The angle formula converts b>=1/3 to Theta<=120 degrees. The apex is the diagonal that controls the admissible CN interval; sufficiently large steps can make the base diagonals negative too, which is compatible with the claimed entrywise-positivity classification.

## originality

PASS

Best-of-knowledge pass for the joint sharp time classification, in particular the 120-degree impossibility threshold and singleton CN interval at equality. Inspected results cover qualitative eventual positivity, sufficient DMP tests, or exact different-matrix thresholds. None inspected gives the necessary-and-sufficient CN interval of the signed three-node Neumann operator. The particularly relevant 2018 Neumann/Robin chapter remains an access limitation.

## value

PASS

The smallest planar Neumann cell with an obtuse angle is a motivated test of whether moving away from small timesteps can restore order preservation. On this symmetric family the complete answer distinguishes BE and heat recovery from CN, which may fail at every nonzero step despite spectral stability. The exact angle marking the loss of feasibility and the singleton boundary matrix make the example useful for testing qualitative mesh and time-step criteria. The value is the precise obstruction and complete window, not the elementary technique of diagonalizing a three-by-three matrix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
