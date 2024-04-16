package clienteChat;

//import java.io.Serializable;
//import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import java.util.Scanner;

import interfaceChat.InterfaceCliente;
import interfaceChat.InterfaceServidor;

public class ClienteChat extends UnicastRemoteObject implements InterfaceCliente {
	private static final long serialVersionUID = 1L;

	protected ClienteChat() throws RemoteException {
        super();
    }

    public void receberMensagem(String mensagem) throws RemoteException {
        System.out.println("Mensagem recebida do " + mensagem);
    }

    public static void main(String[] args) {
        try {
            System.setProperty("java.rmi.server.hostname", "127.0.0.1");
            Registry registro = LocateRegistry.getRegistry("127.0.0.1", 1099);
            InterfaceServidor servidor = (InterfaceServidor) registro.lookup("chat");
            ClienteChat cliente = new ClienteChat();
            servidor.registrarCliente(cliente);

            Scanner scanner = new Scanner(System.in);
            while (true) {
                System.out.print("Digite uma mensagem: ");
                String mensagem = scanner.nextLine();
                servidor.enviarMensagem(mensagem, cliente);
            }
        } catch (Exception e) {
            System.err.println("Erro no Cliente: " + e.toString());
            e.printStackTrace();
        }
    }
}

