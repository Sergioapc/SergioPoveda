#include <iostream>

int main() {
  class IAve
    {
      public: virtual void comer();
    };
  class IAveVoladora
    {
      public: virtual void volar();
    };
  class IAveNadadora
    {
      public: virtual void nadar();
    };

  class Loro: public IAve,IAveVoladora
    {
      public: virtual void comer() override;
      public: virtual void volar() override;
    };
  class Pinguino: public IAve, IAveNadadora
    {
      public: virtual void comer() override;
      public: virtual void nadar() override;
    };
}