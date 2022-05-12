# CTF 192.168.90.82

>### **Scanner (-A)gressivo** 
<br>

<pre>
<font color="#367BF0">┌──(</font><font color="#EC0101"><b>root💀aluno</b></font><font color="#367BF0">)-[</font><b>/home/aluno</b><font color="#367BF0">]</font>
<font color="#367BF0">└─</font><font color="#EC0101"><b>#</b></font> <font color="#5EBDAB">nmap</font> <font color="#9755B3">-A</font> 192.168.90.82 <font color="#9755B3">-p-</font>                                                                                                                                                                                                          <br>
Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-12 13:14 -03
Nmap scan report for 192.168.90.82
Host is up (0.0033s latency).
Not shown: 65531 filtered tcp ports (no-response)
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 4.3p2 Debian 9 (protocol 2.0)
|_auth-owners: root
| ssh-hostkey: 
|   1024 88:23:98:0d:9d:8a:20:59:35:b8:14:12:14:d5:d0:44 (DSA)
|_  2048 6b:5d:04:71:76:78:56:96:56:92:a8:02:30:73:ee:fa (RSA)
113/tcp open  ident
|_auth-owners: identd
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: LOCAL)
|_auth-owners: root
445/tcp open  netbios-ssn Samba smbd 3.0.24 (workgroup: LOCAL)
|_auth-owners: root
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6
OS details: Linux 2.6.15 - 2.6.26 (likely embedded)
Network Distance: 6 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 2h06m26s, deviation: 2h49m43s, median: 6m25s
| smb-security-mode: 
|   account_used: guest
|   authentication_level: share (dangerous)
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_nbstat: NetBIOS name: SOFRIMENTO, NetBIOS user: &lt;unknown&gt;, NetBIOS MAC: &lt;unknown&gt; (unknown)
|_smb2-time: Protocol negotiation failed (SMB2)
<font color="GOLD">| smb-os-discovery: 
|   OS: Unix (Samba 3.0.24)
|   NetBIOS computer name: 
|   Workgroup: THINC.LOCAL\x00
|_  System time: 2022-05-12T12:22:32-04:00</font>

TRACEROUTE (using port 22/tcp)
HOP RTT     ADDRESS
1   0.42 ms 192.168.80.1
2   0.85 ms 192.168.1.2
3   1.14 ms 192.168.1.10
4   2.38 ms 192.168.200.1
5   3.20 ms 192.168.2.70
6   3.24 ms 192.168.90.82

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 147.69 seconds
</pre>

>### **Scanner Direcionado - SMB Discovery** 
<br>
Nesse caso, foi desnecessário, trouxe a mesma resposta do -A anterior:


<pre><font color="#367BF0">┌──(</font><font color="#EC0101"><b>root💀aluno</b></font><font color="#367BF0">)-[</font><b>/home/aluno</b><font color="#367BF0">]</font>
<font color="#367BF0">└─</font><font color="#EC0101"><b>#</b></font> <font color="#5EBDAB"><u style="text-decoration-style:single">sudo</u></font> <font color="#5EBDAB">nmap</font> <font color="#9755B3">-sU</font> <font color="#9755B3">-sS</font> <font color="#9755B3">--script</font> smb-os-discovery.nse <font color="#9755B3">-p</font> U:137,T:139 192.168.90.82

Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-12 13:26 -03
Nmap scan report for 192.168.90.82
Host is up (0.0037s latency).

PORT    STATE SERVICE
139/tcp open  netbios-ssn
137/udp open  netbios-ns

<font color="GOLD">Host script results:
| smb-os-discovery: 
|   OS: Unix (Samba 3.0.24)
|   NetBIOS computer name: 
|   Workgroup: THINC.LOCAL\x00
|_  System time: 2022-05-12T12:33:12-04:00,</font>

Nmap done: 1 IP address (1 host up) scanned in 0.47 seconds
                                                                                                                                                                                                                                               
<font color="#367BF0">┌──(</font><font color="#EC0101"><b>root💀aluno</b></font><font color="#367BF0">)-[</font><b>/home/aluno</b><font color="#367BF0">]</font>
<font color="#367BF0">└─</font><font color="#EC0101"><b>#</b></font> <font color="#5EBDAB">nmap</font> <font color="#9755B3">--script</font> smb-os-discovery.nse <font color="#9755B3">-p445</font>  192.168.90.82

Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-12 13:27 -03
Nmap scan report for 192.168.90.82
Host is up (0.0026s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

<font color="GOLD">Host script results:
| smb-os-discovery: 
|   OS: Unix (Samba 3.0.24)
|   NetBIOS computer name: 
|   Workgroup: THINC.LOCAL\x00
|_  System time: 2022-05-12T12:34:02-04:00</font>

Nmap done: 1 IP address (1 host up) scanned in 0.36 seconds
</pre>

>### **Script para enumeração SAMBA**

<pre><font color="#367BF0">┌──(</font><font color="#EC0101"><b>root💀aluno</b></font><font color="#367BF0">)-[</font><b>/home/aluno</b><font color="#367BF0">]</font>
<font color="#367BF0">└─</font><font color="#EC0101"><b>#</b></font> <font color="#5EBDAB"><u style="text-decoration-style:single">sudo</u></font> <font color="#5EBDAB">nmap</font> <font color="#9755B3">-sU</font> <font color="#9755B3">-sS</font> <font color="#9755B3">--script</font> smb-enum-users.nse <font color="#9755B3">-p</font> U:137,T:139 192.168.90.82 
Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-12 13:30 -03
Nmap scan report for 192.168.90.82
Host is up (0.0026s latency).

PORT    STATE SERVICE
139/tcp open  netbios-ssn
137/udp open  netbios-ns

Host script results:
| <font color="GOLD">smb-enum-users: </font>
|   SOFRIMENTO\backup (RID: 1068)
|     Full name:   backup
|     Flags:       Normal user account
|   SOFRIMENTO\bin (RID: 1004)
|     Full name:   bin
|     Flags:       Normal user account
|   SOFRIMENTO\bob (RID: 3002)
|     Flags:       Normal user account
|   SOFRIMENTO\daemon (RID: 1002)
|     Full name:   daemon
|     Flags:       Normal user account
|   SOFRIMENTO\Debian-exim (RID: 1200)
|     Flags:       Normal user account
|   SOFRIMENTO\games (RID: 1010)
|     Full name:   games
|     Flags:       Normal user account
|   SOFRIMENTO\gnats (RID: 1082)
|     Full name:   Gnats Bug-Reporting System <font color="GOLD">(admin)</font>
|     Flags:       Normal user account
|   SOFRIMENTO\identd (RID: 1204)
|     Flags:       Normal user account
|   SOFRIMENTO\irc (RID: 1078)
|     Full name:   ircd
|     Flags:       Normal user account
|   SOFRIMENTO\list (RID: 1076)
|     Full name:   Mailing List Manager
|     Flags:       Normal user account
|   SOFRIMENTO\lp (RID: 1014)
|     Full name:   lp
|     Flags:       Normal user account
|   SOFRIMENTO\mail (RID: 1016)
|     Full name:   mail
|     Flags:       Normal user account
|   SOFRIMENTO\man (RID: 1012)
|     Full name:   man
|     Flags:       Normal user account
|   SOFRIMENTO\news (RID: 1018)
|     Full name:   news
|     Flags:       Normal user account
|   SOFRIMENTO\nobody (RID: 501)
|     Full name:   nobody
|     Flags:       Normal user account
|   SOFRIMENTO\proxy (RID: 1026)
|     Full name:   proxy
|     Flags:       Normal user account
|   SOFRIMENTO\root (RID: 1000)
|     Full name:   root
|     Flags:       Normal user account
|   SOFRIMENTO\sshd (RID: 1206)
|     Flags:       Normal user account
|   SOFRIMENTO\statd (RID: 1202)
|     Flags:       Normal user account
|   SOFRIMENTO\sync (RID: 1008)
|     Full name:   sync
|     Flags:       Normal user account
|   SOFRIMENTO\sys (RID: 1006)
|     Full name:   sys
|     Flags:       Normal user account
|   SOFRIMENTO\uucp (RID: 1020)
|     Full name:   uucp
|     Flags:       Normal user account
|   SOFRIMENTO\www-data (RID: 1066)
|     Full name:   www-data
|_    Flags:       Normal user account

Nmap done: 1 IP address (1 host up) scanned in 0.61 seconds
</pre>

>### **Tentando logar com algum usuário:**

<pre><font color="#367BF0">┌──(</font><font color="#EC0101"><b>root💀aluno</b></font><font color="#367BF0">)-[</font><b>/home/aluno</b><font color="#367BF0">]</font>
<font color="#367BF0">└─</font><font color="#EC0101"><b>#</b></font> <font color="#5EBDAB">smbclient</font> <font color="#9755B3">-L</font> 192.168.90.82 <font color="#9755B3">-U</font> admin                                                     

Enter WORKGROUP\admin&apos;s password: 

	Sharename       Type      Comment
	---------       ----      -------
	IPC$            IPC       IPC Service (sofrimento debian server)
	<font color="GOLD">Bob Share       Disk      Bob Docs</font>
	print$          Disk      Printer Drivers
Reconnecting with SMB1 for workgroup listing.

	Server               Comment
	---------            -------
	SOFRIMENTO           sofrimento debian server

	Workgroup            Master
	---------            -------
	CYBERTRON2           ECO
	MYGROUP              DIVERSE
	SECURITY             102GAAAE
	THINC.LOCAL          SOFRIMENTO
	WORKGROUP            ALFREDO-PC
</pre>

>### **Entrando no SAMBA via "Linux Explorer"**
<br>

Diretório sem senha, basta digitar na barra de endereços:

    smb://192.168.90.82/bob share/

É possível navegar livremente até a primeira flag:

    smb://192.168.90.82/bob share/rootdir/home/flag.txt

E também podemos navegar livremente até a segunda flag:

    smb://192.168.90.82/bob share/rootdir/root/flag.txt