package interfaceChat;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface InterfaceCliente extends Remote {
	
    void receberMensagem(String mensagem) throws RemoteException;
    
}