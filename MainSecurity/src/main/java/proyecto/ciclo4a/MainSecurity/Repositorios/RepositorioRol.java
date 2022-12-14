package proyecto.ciclo4a.MainSecurity.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import proyecto.ciclo4a.MainSecurity.Modelos.Rol;

public interface RepositorioRol extends MongoRepository<Rol, String> {
}
