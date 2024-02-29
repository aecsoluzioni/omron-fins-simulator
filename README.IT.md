## SIMULATORE DI PINNE OMRON.

## Cos'è questo.

Si tratta di uno script per eseguire un PC con Ruby come PLC virtuale.
È stato implementato per eseguire il debug di un programma che comunica con un PLC tramite il protocollo FINS.

Appena avviato, si mette in ascolto su un socket UDP sulla porta specificata (default: 9600) e restituisce una risposta a una richiesta tramite il protocollo FINS.
Attualmente sono supportate solo l'acquisizione e la scrittura dell'area DM e l'acquisizione di data e ora. Il protocollo TCP non è supportato.

## Ambiente di esecuzione.

* `Ruby 1.8` o superiore, testato su Linux, MacOSX, funzionerà anche su Windows.
* Il PC che esegue questo script e il PC comunicante devono trovarsi in un ambiente di rete in cui possono comunicare tra loro sulla porta UDP 9600 (o sulla porta specificata con `--port`).

## Installazione.

Si prega di clonare `git` questo progetto a mano.

```
$ git clone https://github.com/hiroeorz/omron-fins-simulator.git
```

L'unico file da eseguire è `omron_plc.rb`, che può essere eseguito così com'è o copiato in una cartella adatta ed eseguito.

```
$ ruby omron_plc.rb --address=<il vostro indirizzo IP> --port=<porta>
```

Esempio di esecuzione:.

```
$ cd omron-fins-simulator
$ ruby omron_plc.rb --address=192.168.0.6 --port=9600
```

Altre opzioni sono.

```
$ ruby omron_plc.rb --address=192.168.0.6 --port=9600 --count_up_dm=5095 --countup_interval=5 --load_file=/tmp/dm.yaml
```

* `--address` : proprio indirizzo IP. Il valore predefinito è `127.0.0.1`.
* `--port` : numero di porta. Il valore predefinito è `9600`.
* `--count_up_dm` : Specifica il numero di DM da contare automaticamente. È possibile specificare più numeri separandoli con delle virgole.
    * Esempio di specificazione multipla: `--count_up_dm=1,2,3`.
* `--countup_interval` : Specifica l'intervallo per il conteggio automatico. L'impostazione predefinita è 5 secondi.
* `--load_file` : file di configurazione del DM da caricare all'avvio. Se non viene specificato, tutti i DM sono inizialmente `0`.
    * Il formato del file di configurazione è YAML, dove la chiave è il numero del DM e il valore è il valore del DM.

        ``` 
        3: 0
        100: 11
        101: 21
        102: 0xff
        103: 0x10
        ``` 

### Imposta e recupera i valori in modo interattivo.

Quando viene attivato, il sistema inizia ad accettare pacchetti UDP sulla porta specificata e attende un input sulla console.

```
$ ruby omron_plc.rb --address=192.168.0.6 --port=9600

Loading /tmp/test.yaml...done
UDP Socket bind to host:192.168.0.6, port:9600.

----------------------------------------------------
PLC SIMULATOR SYSTEM
----------------------------------------------------
SET DM COMMAND     : > set <dm number>, <value>
GET DM COMMAND     : > get <dm number>
GET DM LIST COMMAND: > get_list <dm number>, <count>
EXIT COMMAND       : > exit
----------------------------------------------------

> 
```

Quando viene visualizzato `>`, come sopra, sono disponibili diversi comandi.

#### Impostazione dei valori nell'area DM.

```
> set <numero DM>, <valore>
```

#### Leggere il valore di un'area DM.

```
> get <numero DM>
<valore di visualizzazione>
```

#### Leggere i valori di più aree DM contemporaneamente

```
> get_list <dm numero>, <count>
<dm numero 1> : valore
<DM numero 2> : valore
<Numero 3> : valore
```

#### Fine del programma

```
> exit
```

#### Esempio di esecuzione

```
$ ruby omron_plc.rb --address=192.168.0.6 --port=9600

Loading /tmp/test.yaml...done
UDP Socket bind to host:172.16.15.35, port:9600.

----------------------------------------------------
PLC SIMULATOR SYSTEM
----------------------------------------------------
SET DM COMMAND     : > set <dm number>, <value>
GET DM COMMAND     : > get <dm number>
GET DM LIST COMMAND: > get_list <dm number>, <count>
EXIT COMMAND       : > exit
----------------------------------------------------

> 
> set 1, 100
ok

> set 2, 200
ok

> set 3, 300
ok

> get_list 1, 3
1 : 100
2 : 200
3 : 300

> exit

$
```