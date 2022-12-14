package proyecto.ciclo4a.MainSecurity.Repositorios;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;
import proyecto.ciclo4a.MainSecurity.Modelos.Usuario;

public interface RepositorioUsuario extends MongoRepository<Usuario, String>{
    @Query("{'correo':?0}")
    public Usuario getUserByMail(String correo);    
}
