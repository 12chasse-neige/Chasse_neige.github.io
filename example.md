## Final Review of Advanced Calculus  


### 1. Taylor's Theorem
#### 1.1 Taylor's Theorem with Peano's Form of Remainder

When \( f(x) \) is n times differentiable on an open interval \( I \) containing the point \( a \)

\[ 
f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n + o((x-a)^n) 
\]

Specially, when $ a=0 $, the polnomial

\[ 
f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \cdots + \frac{f^{(n)}(0)}{n!}x^n + o(x^n) 
\]

is called Maclaurin's polnomial.

#### 1.2 Taylor's Theorem with Lagrange's Form of Remainder

If a function \( f(x) \) is \( (n+1) \) times differentiable on an open interval \( I \) containing the point \( a \), then for any \( x \) in \( I \), there exists a point \( c \) between \( a \) and \( x \) such that:

\[
f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \cdots + \frac{f^{(n)}(a)}{n!}(x-a)^n + R_n(x)
\]

where \( R_n(x) \) is the remainder term given by:

\[
R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}
\]

Here, \( c \) is some point between \( a \) and \( x \). The remainder term \( R_n(x) \) represents the error in approximating \( f(x) \) by the \( n \)-th degree Taylor polynomial centered at \( a \). The form of the remainder provided by Lagrange gives a specific way to bound this error, depending on the \((n+1)\)-th derivative of \( f \) at some point \( c \) in the interval.
##### Proof.
Given that \( f(x) \) is \( (n+1) \) times differentiable, then we can use the Cauchy's Mean Value Theorem on the functions \( F(t) = f(x+t \Delta x) - P_{n}(t \Delta x) \) and \( G(t) = (t \Delta x)^{n+1} \), where \( t \) is an arbitrary constant between \( 0 \) and \( 1 \)

\[ 
\frac{F(t)-F(0)}{G(t)-G(0)} = \frac{(f'(x+t_{1} \Delta x) - P_{n}'(t_{1} \Delta x)) \Delta x}{(n+1)(t_{1} \Delta x)^{n} \Delta x} = \ldots = \frac{f^{(n)}(x+t_{n} \Delta x) - P_{n}^{(n)}(t_{n} \Delta x)}{(n+1)!} 
\] 

then let \( t=1 \) and we can get the Lagrange's form.

#### 1.3  Taylor's Theorem with Cauchy's Form of Remainder

Cauchy's Form of the Remainder is anither way to express the remainder term \( R_n(x) \). It states that:

\[ R_n(x) = \frac{f^{(n+1)}(c)}{n!}(x-c)^n(x-a) \]

where \( c \) is some number between \( a \) and \( x \) .
##### Proof.



##### Applications:
Using the Taylor's theorem with Lagrange's form of remainder to estimate the Taylor series's error.
###### EX.1
Given that\( f \in C^{3}[a-h, a+h] \), \( h > 0  \) and \( \lvert f(x) \rvert \leq M \), prove that 

\[ 
\lvert \frac{f(a+h)+f(a-h)-2f(a)}{h^2} - f''(a) \rvert \leq \frac{Mh}{3} 
\]

###### Proof.
First use \(f\)'s Taylor Series about a:

\[ 
f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2}(x-a)^2 + o((x-a)^2) 
\]

so it is trivial that 

\[ 
f(a+h) = f(a) + f'(a)h + \frac{f''(a)}{2}h^2 + o(h^2) 
\]

\[ 
f(a-h) = f(a) - f'(a)h + \frac{f''(a)}{2}h^2 + o(h^2) 
\]

so \[ f(a+h) + f(a-h) - 2f(a) = 2\]


