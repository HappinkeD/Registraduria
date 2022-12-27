package proyecto.ciclo4a.MainSecurity.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;
import proyecto.ciclo4a.MainSecurity.Modelos.Permiso;

public interface RepositorioPermiso extends MongoRepository<Permiso, String> {
    @Query("{'url':?0, 'metodo':?1}")
    Permiso getPermiso(String url, String metodo);
}
