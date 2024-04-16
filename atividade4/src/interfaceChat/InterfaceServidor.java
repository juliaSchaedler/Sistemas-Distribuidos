package interfaceChat;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface InterfaceServidor extends Remote {
	
    void enviarMensagem(String mensagem, InterfaceCliente cliente) throws RemoteException;
    void registrarCliente(InterfaceCliente cliente) throws RemoteException;
    
}