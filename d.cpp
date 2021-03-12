#include <iostream>

int main() {
  class Dato{

  };
  class Conexion
    {
      public: 
      virtual Dato getDatos();
      virtual void setDatos();
    };

  class AccesoADatos
    {
      private: Conexion conexion;
      public: AccesoADatos(Conexion conect){
        conexion=conect;
      }
      Dato getDatos(){
        conexion.getDatos();
      }
    };
 
  class dataBaseService: public Conexion
  {
    public: 
      virtual Dato getDatos() override;
      virtual void setDatos() override;
  };
}