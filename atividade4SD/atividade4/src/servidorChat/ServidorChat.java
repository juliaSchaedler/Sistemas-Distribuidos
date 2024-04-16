package servidorChat;

import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import java.util.Scanner;
import interfaceChat.InterfaceCliente;
import interfaceChat.InterfaceServidor;

public class ServidorChat extends UnicastRemoteObject implements InterfaceServidor {

    private InterfaceCliente cliente1;
    private InterfaceCliente cliente2;

    protected ServidorChat() throws RemoteException {
        super();
    }

    public void enviarMensagem(String mensagem, InterfaceCliente cliente) throws RemoteException {
        if (cliente1 != null && cliente2 != null) {
            if (cliente.equals(cliente1)) {
                cliente2.receberMensagem("Cliente 1: " + mensagem);
            } else if (cliente.equals(cliente2)) {
                cliente1.receberMensagem("Cliente 2: " + mensagem);
            }
        }
    }

    public void registrarCliente(InterfaceCliente cliente) throws RemoteException {
        if (cliente1 == null) {
            cliente1 = cliente;
        } else if (cliente2 == null) {
            cliente2 = cliente;
        }
    }

    public static void main(String[] args) {
        try {
            System.setProperty("java.rmi.server.hostname", "127.0.0.1");
            ServidorChat servidor = new ServidorChat();
            Registry registro = LocateRegistry.createRegistry(1099);
            registro.rebind("chat", servidor);
            System.out.println("Servidor de Chat pronto!");
        } catch (Exception e) {
            System.err.println("Erro no Servidor de Chat: " + e.toString());
            e.printStackTrace();
        }
    }
}