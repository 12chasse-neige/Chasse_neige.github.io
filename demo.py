class A:
    n = 42
    def f(self) -> str:
      return f"I'm {self.n}!"
a = A()
A.n = 21
print(A.f(a))