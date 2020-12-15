rule file_blocker : fh.exe
{
    meta:malware detection exe
        description = "This is just an example"
        threat_level = 1
        in_the_wild = true
    strings:
        $a = {4D 5A 90 00 03 00 00 00 04 00 00 00 FF FF 00 00 B8 00 00 00 00 00 00 40 00 00 00 00 00 }
        $b = "51D6E4C3507D6AD080DA3D4676E12B9D9"
       
    condition:
        $a or $b
}