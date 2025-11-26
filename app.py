from itertools import count
from flask import Flask, render_template, url_for, request, Response, jsonify
import numpy as np
import database
import prediction
import json
import io
import random
import visualization
from pymongo import MongoClient
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import modelbuild
from datetime import datetime

{
    "t": {"$date": "2025-11-23T02:47:40.039+05:30"},
    "s": "I",
    "c": "-",
    "id": 8991200,
    "ctx": "thread1",
    "msg": "Shuffling initializers",
    "attr": {"seed": 4095822582},
}
{
    "t": {"$date": "2025-11-23T02:47:40.238+05:30"},
    "s": "I",
    "c": "CONTROL",
    "id": 97374,
    "ctx": "thread1",
    "msg": "Automatically disabling TLS 1.0 and TLS 1.1, to force-enable TLS 1.1 specify --sslDisabledProtocols 'TLS1_0'; to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'",
}
{
    "t": {"$date": "2025-11-23T02:47:40.251+05:30"},
    "s": "I",
    "c": "NETWORK",
    "id": 4915701,
    "ctx": "thread1",
    "msg": "Initialized wire specification",
    "attr": {
        "spec": {
            "incomingExternalClient": {"minWireVersion": 0, "maxWireVersion": 27},
            "incomingInternalClient": {"minWireVersion": 0, "maxWireVersion": 27},
            "outgoing": {"minWireVersion": 6, "maxWireVersion": 27},
            "isInternalClient": true,
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.252+05:30"},
    "s": "I",
    "c": "CONTROL",
    "id": 5945603,
    "ctx": "thread1",
    "msg": "Multi threading initialized",
}
{
    "t": {"$date": "2025-11-23T02:47:40.252+05:30"},
    "s": "I",
    "c": "CONTROL",
    "id": 4615611,
    "ctx": "initandlisten",
    "msg": "MongoDB starting",
    "attr": {
        "pid": 2548,
        "port": 27017,
        "dbPath": "/data/db",
        "architecture": "64-bit",
        "host": "BT-2204030",
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.252+05:30"},
    "s": "I",
    "c": "CONTROL",
    "id": 23398,
    "ctx": "initandlisten",
    "msg": "Target operating system minimum version",
    "attr": {"targetMinOS": "Windows 7/Windows Server 2008 R2"},
}
{
    "t": {"$date": "2025-11-23T02:47:40.253+05:30"},
    "s": "I",
    "c": "CONTROL",
    "id": 23403,
    "ctx": "initandlisten",
    "msg": "Build Info",
    "attr": {
        "buildInfo": {
            "version": "8.2.2",
            "gitVersion": "594f839ceec1f4385be9a690131412d67b249a0a",
            "modules": [],
            "allocator": "tcmalloc-gperf",
            "environment": {"distmod": "windows"},
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.253+05:30"},
    "s": "I",
    "c": "CONTROL",
    "id": 51765,
    "ctx": "initandlisten",
    "msg": "Operating System",
    "attr": {
        "os": {
            "name": "Microsoft Windows Workstation (build 26200)",
            "version": "10.0 (build 26200)",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.254+05:30"},
    "s": "I",
    "c": "CONTROL",
    "id": 21951,
    "ctx": "initandlisten",
    "msg": "Options set by command line",
    "attr": {"options": {}},
}
{
    "t": {"$date": "2025-11-23T02:47:40.255+05:30"},
    "s": "I",
    "c": "NETWORK",
    "id": 4648601,
    "ctx": "initandlisten",
    "msg": "Implicit TCP FastOpen unavailable. If TCP FastOpen is required, set at least one of the related parameters",
    "attr": {
        "relatedParameters": [
            "tcpFastOpenServer",
            "tcpFastOpenClient",
            "tcpFastOpenQueueSize",
        ]
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.268+05:30"},
    "s": "I",
    "c": "STORAGE",
    "id": 22315,
    "ctx": "initandlisten",
    "msg": "Opening WiredTiger",
    "attr": {
        "config": "create,cache_size=7453M,session_max=33000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,remove=true,path=journal,compressor=snappy),builtin_extension_config=(zstd=(compression_level=6)),file_manager=(close_idle_time=600,close_scan_interval=10,close_handle_minimum=2000),statistics_log=(wait=0),json_output=(error,message),verbose=[recovery_progress:1,checkpoint_progress:1,compact_progress:1,live_restore_progress:1,backup:0,checkpoint:0,compact:0,eviction:0,fileops:0,history_store:0,live_restore:0,recovery:0,rts:0,salvage:0,tiered:0,timestamp:0,transaction:0,verify:0,log:0],prefetch=(available=true,default=false),"
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.278+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 278419,
            "thread": "2548:140730925155872",
            "session_name": "wiredtiger_open",
            "category": "WT_VERB_RECOVERY",
            "log_id": 1000000,
            "category_id": 32,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "opening the WiredTiger library",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.312+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 312039,
            "thread": "2548:140730925155872",
            "session_name": "connection",
            "category": "WT_VERB_RECOVERY",
            "log_id": 1000000,
            "category_id": 32,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "connection configuration string parsing completed",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.399+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 398753,
            "thread": "2548:140730925155872",
            "session_name": "connection",
            "category": "WT_VERB_RECOVERY",
            "log_id": 1000000,
            "category_id": 32,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "starting WiredTiger utility threads",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.447+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 446178,
            "thread": "2548:140730925155872",
            "session_name": "connection",
            "category": "WT_VERB_RECOVERY",
            "log_id": 1000000,
            "category_id": 32,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "starting WiredTiger recovery",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.448+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 448715,
            "thread": "2548:140730925155872",
            "session_name": "txn-recover",
            "category": "WT_VERB_RECOVERY",
            "log_id": 1000000,
            "category_id": 32,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "scanning metadata to find the largest file ID",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.451+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 450719,
            "thread": "2548:140730925155872",
            "session_name": "txn-recover",
            "category": "WT_VERB_RECOVERY",
            "log_id": 1000000,
            "category_id": 32,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "largest file ID found in the metadata 0",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.451+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 450719,
            "thread": "2548:140730925155872",
            "session_name": "txn-recover",
            "category": "WT_VERB_RECOVERY",
            "log_id": 1000000,
            "category_id": 32,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "recovery log replay has successfully finished and ran for 3 milliseconds",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.451+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 451715,
            "thread": "2548:140730925155872",
            "session_name": "txn-recover",
            "category": "WT_VERB_RECOVERY_PROGRESS",
            "log_id": 1000000,
            "category_id": 33,
            "verbose_level": "DEBUG_1",
            "verbose_level_id": 1,
            "msg": "Set global recovery timestamp: (0, 0)",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.452+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 451715,
            "thread": "2548:140730925155872",
            "session_name": "txn-recover",
            "category": "WT_VERB_RECOVERY_PROGRESS",
            "log_id": 1000000,
            "category_id": 33,
            "verbose_level": "DEBUG_1",
            "verbose_level_id": 1,
            "msg": "Set global oldest timestamp: (0, 0)",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.454+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 454098,
            "thread": "2548:140730925155872",
            "session_name": "txn-recover",
            "category": "WT_VERB_RECOVERY",
            "log_id": 1493201,
            "category_id": 32,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "recovery was completed successfully and took 6ms, including 3ms for the log replay, 0ms for the rollback to stable, and 0ms for the checkpoint.",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.455+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 454098,
            "thread": "2548:140730925155872",
            "session_name": "txn-recover",
            "category": "WT_VERB_RECOVERY_PROGRESS",
            "log_id": 1493201,
            "category_id": 33,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "recovery was completed successfully and took 6ms, including 3ms for the log replay, 0ms for the rollback to stable, and 0ms for the checkpoint.",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.470+05:30"},
    "s": "I",
    "c": "WTEVICT",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 468664,
            "thread": "2548:140730925155872",
            "session_name": "connection",
            "category": "WT_VERB_EVICTION",
            "log_id": 1000000,
            "category_id": 15,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "starting eviction threads",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.481+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 480767,
            "thread": "2548:140730925155872",
            "session_name": "connection",
            "category": "WT_VERB_RECOVERY",
            "log_id": 1000000,
            "category_id": 32,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "WiredTiger utility threads started successfully",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.481+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 480767,
            "thread": "2548:140730925155872",
            "session_name": "connection",
            "category": "WT_VERB_RECOVERY",
            "log_id": 1000000,
            "category_id": 32,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "the WiredTiger library has successfully opened",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.482+05:30"},
    "s": "I",
    "c": "STORAGE",
    "id": 4795906,
    "ctx": "initandlisten",
    "msg": "WiredTiger opened",
    "attr": {"durationMillis": 213},
}
{
    "t": {"$date": "2025-11-23T02:47:40.482+05:30"},
    "s": "I",
    "c": "RECOVERY",
    "id": 23987,
    "ctx": "initandlisten",
    "msg": "WiredTiger recoveryTimestamp",
    "attr": {"recoveryTimestamp": {"$timestamp": {"t": 0, "i": 0}}},
}
{
    "t": {"$date": "2025-11-23T02:47:40.482+05:30"},
    "s": "I",
    "c": "STORAGE",
    "id": 9086700,
    "ctx": "initandlisten",
    "msg": "WiredTiger session cache max value has been set",
    "attr": {"sessionCacheMax": 16500},
}
{
    "t": {"$date": "2025-11-23T02:47:40.499+05:30"},
    "s": "I",
    "c": "STORAGE",
    "id": 10158000,
    "ctx": "initandlisten",
    "msg": "Opening spill WiredTiger",
    "attr": {
        "config": "create,cache_size=398M,session_max=1024,eviction=(threads_min=1,threads_max=1),eviction_dirty_target=19MB,eviction_dirty_trigger=318MB,eviction_updates_trigger=318MB,config_base=false,statistics=(fast),log=(enabled=false),builtin_extension_config=(zstd=(compression_level=-7)),file_manager=(close_idle_time=600,close_scan_interval=10,close_handle_minimum=2000),statistics_log=(wait=0),json_output=(error,message),verbose=[recovery_progress:1,checkpoint_progress:1,compact_progress:1,live_restore_progress:1,backup:0,checkpoint:0,compact:0,eviction:0,fileops:0,history_store:0,live_restore:0,recovery:0,rts:0,salvage:0,tiered:0,timestamp:0,transaction:0,verify:0,log:0],"
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.508+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 507859,
            "thread": "2548:140730925155872",
            "session_name": "wiredtiger_open",
            "category": "WT_VERB_RECOVERY",
            "log_id": 1000000,
            "category_id": 32,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "opening the WiredTiger library",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.512+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 511856,
            "thread": "2548:140730925155872",
            "session_name": "connection",
            "category": "WT_VERB_RECOVERY",
            "log_id": 1000000,
            "category_id": 32,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "connection configuration string parsing completed",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.526+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 525896,
            "thread": "2548:140730925155872",
            "session_name": "connection",
            "category": "WT_VERB_RECOVERY",
            "log_id": 1000000,
            "category_id": 32,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "starting WiredTiger utility threads",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.527+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 526905,
            "thread": "2548:140730925155872",
            "session_name": "connection",
            "category": "WT_VERB_RECOVERY",
            "log_id": 1000000,
            "category_id": 32,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "starting WiredTiger recovery",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.530+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 529905,
            "thread": "2548:140730925155872",
            "session_name": "txn-recover",
            "category": "WT_VERB_RECOVERY",
            "log_id": 1000000,
            "category_id": 32,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "scanning metadata to find the largest file ID",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.530+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 529905,
            "thread": "2548:140730925155872",
            "session_name": "txn-recover",
            "category": "WT_VERB_RECOVERY",
            "log_id": 1000000,
            "category_id": 32,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "largest file ID found in the metadata 0",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.530+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 529905,
            "thread": "2548:140730925155872",
            "session_name": "txn-recover",
            "category": "WT_VERB_RECOVERY",
            "log_id": 1000000,
            "category_id": 32,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "recovery log replay has successfully finished and ran for 0 milliseconds",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.530+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 530903,
            "thread": "2548:140730925155872",
            "session_name": "txn-recover",
            "category": "WT_VERB_RECOVERY_PROGRESS",
            "log_id": 1000000,
            "category_id": 33,
            "verbose_level": "DEBUG_1",
            "verbose_level_id": 1,
            "msg": "Set global recovery timestamp: (0, 0)",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.531+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 530903,
            "thread": "2548:140730925155872",
            "session_name": "txn-recover",
            "category": "WT_VERB_RECOVERY_PROGRESS",
            "log_id": 1000000,
            "category_id": 33,
            "verbose_level": "DEBUG_1",
            "verbose_level_id": 1,
            "msg": "Set global oldest timestamp: (0, 0)",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.531+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 530903,
            "thread": "2548:140730925155872",
            "session_name": "txn-recover",
            "category": "WT_VERB_RECOVERY",
            "log_id": 1493201,
            "category_id": 32,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "recovery was completed successfully and took 1ms, including 0ms for the log replay, 0ms for the rollback to stable, and 0ms for the checkpoint.",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.532+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 531903,
            "thread": "2548:140730925155872",
            "session_name": "txn-recover",
            "category": "WT_VERB_RECOVERY_PROGRESS",
            "log_id": 1493201,
            "category_id": 33,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "recovery was completed successfully and took 1ms, including 0ms for the log replay, 0ms for the rollback to stable, and 0ms for the checkpoint.",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.578+05:30"},
    "s": "I",
    "c": "WTEVICT",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 578066,
            "thread": "2548:140730925155872",
            "session_name": "connection",
            "category": "WT_VERB_EVICTION",
            "log_id": 1000000,
            "category_id": 15,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "starting eviction threads",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.579+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 578066,
            "thread": "2548:140730925155872",
            "session_name": "connection",
            "category": "WT_VERB_RECOVERY",
            "log_id": 1000000,
            "category_id": 32,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "WiredTiger utility threads started successfully",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.580+05:30"},
    "s": "I",
    "c": "WTRECOV",
    "id": 22430,
    "ctx": "initandlisten",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846260,
            "ts_usec": 580065,
            "thread": "2548:140730925155872",
            "session_name": "connection",
            "category": "WT_VERB_RECOVERY",
            "log_id": 1000000,
            "category_id": 32,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "the WiredTiger library has successfully opened",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.580+05:30"},
    "s": "I",
    "c": "STORAGE",
    "id": 10158001,
    "ctx": "initandlisten",
    "msg": "Spill WiredTiger opened",
    "attr": {"durationMillis": 79},
}
{
    "t": {"$date": "2025-11-23T02:47:40.588+05:30"},
    "s": "I",
    "c": "STORAGE",
    "id": 9529901,
    "ctx": "initandlisten",
    "msg": "Initializing durable catalog",
    "attr": {"numRecords": 0},
}
{
    "t": {"$date": "2025-11-23T02:47:40.589+05:30"},
    "s": "I",
    "c": "STORAGE",
    "id": 9529902,
    "ctx": "initandlisten",
    "msg": "Retrieving all idents from storage engine",
}
{
    "t": {"$date": "2025-11-23T02:47:40.589+05:30"},
    "s": "I",
    "c": "STORAGE",
    "id": 9529903,
    "ctx": "initandlisten",
    "msg": "Initializing all collections in durable catalog",
    "attr": {"numEntries": 0},
}
{
    "t": {"$date": "2025-11-23T02:47:40.624+05:30"},
    "s": "W",
    "c": "CONTROL",
    "id": 22120,
    "ctx": "initandlisten",
    "msg": "Access control is not enabled for the database. Read and write access to data and configuration is unrestricted",
    "tags": ["startupWarnings"],
}
{
    "t": {"$date": "2025-11-23T02:47:40.625+05:30"},
    "s": "W",
    "c": "CONTROL",
    "id": 22140,
    "ctx": "initandlisten",
    "msg": "This server is bound to localhost. Remote systems will be unable to connect to this server. Start the server with --bind_ip <address> to specify which IP addresses it should serve responses from, or with --bind_ip_all to bind to all interfaces. If this behavior is desired, start the server with --bind_ip 127.0.0.1 to disable this warning",
    "tags": ["startupWarnings"],
}
{
    "t": {"$date": "2025-11-23T02:47:40.627+05:30"},
    "s": "I",
    "c": "STORAGE",
    "id": 20320,
    "ctx": "initandlisten",
    "msg": "createCollection",
    "attr": {
        "namespace": "admin.system.version",
        "uuidDisposition": "provided",
        "uuid": {"uuid": {"$uuid": "b4bfec42-ff02-4f8e-80c3-029be0dd0113"}},
        "options": {"uuid": {"$uuid": "b4bfec42-ff02-4f8e-80c3-029be0dd0113"}},
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.655+05:30"},
    "s": "I",
    "c": "INDEX",
    "id": 20345,
    "ctx": "initandlisten",
    "msg": "Index build: done building",
    "attr": {
        "buildUUID": null,
        "collectionUUID": {"uuid": {"$uuid": "b4bfec42-ff02-4f8e-80c3-029be0dd0113"}},
        "namespace": "admin.system.version",
        "index": "_id_",
        "ident": "index-139e272f-74f3-4768-a407-c69d124cbaf4",
        "collectionIdent": "collection-a7d9c428-2a17-41bd-a747-e46da673e416",
        "commitTimestamp": null,
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.657+05:30"},
    "s": "I",
    "c": "REPL",
    "id": 20459,
    "ctx": "initandlisten",
    "msg": "Setting featureCompatibilityVersion",
    "attr": {"newVersion": "8.2"},
}
{
    "t": {"$date": "2025-11-23T02:47:40.659+05:30"},
    "s": "I",
    "c": "REPL",
    "id": 5853300,
    "ctx": "initandlisten",
    "msg": "current featureCompatibilityVersion value",
    "attr": {"featureCompatibilityVersion": "8.2", "context": "setFCV"},
}
{
    "t": {"$date": "2025-11-23T02:47:40.660+05:30"},
    "s": "I",
    "c": "NETWORK",
    "id": 4915702,
    "ctx": "initandlisten",
    "msg": "Updated wire specification",
    "attr": {
        "oldSpec": {
            "incomingExternalClient": {"minWireVersion": 0, "maxWireVersion": 27},
            "incomingInternalClient": {"minWireVersion": 0, "maxWireVersion": 27},
            "outgoing": {"minWireVersion": 6, "maxWireVersion": 27},
            "isInternalClient": true,
        },
        "newSpec": {
            "incomingExternalClient": {"minWireVersion": 0, "maxWireVersion": 27},
            "incomingInternalClient": {"minWireVersion": 27, "maxWireVersion": 27},
            "outgoing": {"minWireVersion": 27, "maxWireVersion": 27},
            "isInternalClient": true,
        },
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.660+05:30"},
    "s": "I",
    "c": "NETWORK",
    "id": 4915702,
    "ctx": "initandlisten",
    "msg": "Updated wire specification",
    "attr": {
        "oldSpec": {
            "incomingExternalClient": {"minWireVersion": 0, "maxWireVersion": 27},
            "incomingInternalClient": {"minWireVersion": 27, "maxWireVersion": 27},
            "outgoing": {"minWireVersion": 27, "maxWireVersion": 27},
            "isInternalClient": true,
        },
        "newSpec": {
            "incomingExternalClient": {"minWireVersion": 0, "maxWireVersion": 27},
            "incomingInternalClient": {"minWireVersion": 27, "maxWireVersion": 27},
            "outgoing": {"minWireVersion": 27, "maxWireVersion": 27},
            "isInternalClient": true,
        },
    },
}
{
    "t": {"$date": "2025-11-23T02:47:40.661+05:30"},
    "s": "I",
    "c": "REPL",
    "id": 5853300,
    "ctx": "initandlisten",
    "msg": "current featureCompatibilityVersion value",
    "attr": {"featureCompatibilityVersion": "8.2", "context": "startup"},
}
{
    "t": {"$date": "2025-11-23T02:47:40.662+05:30"},
    "s": "I",
    "c": "STORAGE",
    "id": 5071100,
    "ctx": "initandlisten",
    "msg": "Clearing temp directory",
}
{
    "t": {"$date": "2025-11-23T02:47:40.664+05:30"},
    "s": "I",
    "c": "STORAGE",
    "id": 10682200,
    "ctx": "initandlisten",
    "msg": "Dropping spill idents",
    "attr": {"numIdents": 0},
}
{
    "t": {"$date": "2025-11-23T02:47:40.664+05:30"},
    "s": "I",
    "c": "CONTROL",
    "id": 6608200,
    "ctx": "initandlisten",
    "msg": "Initializing cluster server parameters from disk",
}
{
    "t": {"$date": "2025-11-23T02:47:40.665+05:30"},
    "s": "I",
    "c": "CONTROL",
    "id": 20536,
    "ctx": "initandlisten",
    "msg": "Flow Control is enabled on this deployment",
}
{
    "t": {"$date": "2025-11-23T02:47:41.240+05:30"},
    "s": "I",
    "c": "FTDC",
    "id": 20625,
    "ctx": "initandlisten",
    "msg": "Initializing full-time diagnostic data capture",
    "attr": {"dataDirectory": "/data/db/diagnostic.data"},
}
{
    "t": {"$date": "2025-11-23T02:47:41.242+05:30"},
    "s": "I",
    "c": "STORAGE",
    "id": 20320,
    "ctx": "initandlisten",
    "msg": "createCollection",
    "attr": {
        "namespace": "local.startup_log",
        "uuidDisposition": "generated",
        "uuid": {"uuid": {"$uuid": "5df029df-9739-4351-ba30-ec7e3af65a43"}},
        "options": {"capped": true, "size": 10485760},
    },
}
{
    "t": {"$date": "2025-11-23T02:47:41.256+05:30"},
    "s": "I",
    "c": "INDEX",
    "id": 20345,
    "ctx": "initandlisten",
    "msg": "Index build: done building",
    "attr": {
        "buildUUID": null,
        "collectionUUID": {"uuid": {"$uuid": "5df029df-9739-4351-ba30-ec7e3af65a43"}},
        "namespace": "local.startup_log",
        "index": "_id_",
        "ident": "index-11372db0-3ae3-47e5-a06b-c2032338559e",
        "collectionIdent": "collection-24fb1e43-56a0-4e5e-bbc4-3d0f9920a49d",
        "commitTimestamp": null,
    },
}
{
    "t": {"$date": "2025-11-23T02:47:41.256+05:30"},
    "s": "I",
    "c": "REPL",
    "id": 6015317,
    "ctx": "initandlisten",
    "msg": "Setting new configuration state",
    "attr": {"newState": "ConfigReplicationDisabled", "oldState": "ConfigPreStart"},
}
{
    "t": {"$date": "2025-11-23T02:47:41.256+05:30"},
    "s": "I",
    "c": "STORAGE",
    "id": 22262,
    "ctx": "initandlisten",
    "msg": "Timestamp monitor starting",
}
{
    "t": {"$date": "2025-11-23T02:47:41.257+05:30"},
    "s": "I",
    "c": "STORAGE",
    "id": 7333401,
    "ctx": "initandlisten",
    "msg": "Starting the DiskSpaceMonitor",
}
{
    "t": {"$date": "2025-11-23T02:47:41.265+05:30"},
    "s": "I",
    "c": "NETWORK",
    "id": 23015,
    "ctx": "listener",
    "msg": "Listening on",
    "attr": {"address": "127.0.0.1:27017"},
}
{
    "t": {"$date": "2025-11-23T02:47:41.266+05:30"},
    "s": "I",
    "c": "NETWORK",
    "id": 23016,
    "ctx": "listener",
    "msg": "Waiting for connections",
    "attr": {"port": 27017, "ssl": "off"},
}
{
    "t": {"$date": "2025-11-23T02:47:41.266+05:30"},
    "s": "I",
    "c": "CONTROL",
    "id": 8423403,
    "ctx": "initandlisten",
    "msg": "mongod startup complete",
    "attr": {
        "Summary of time elapsed": {
            "Startup from clean shutdown?": true,
            "Statistics": {
                "setUpPeriodicRunnerMillis": 0,
                "setUpOCSPMillis": 0,
                "setUpTransportLayerMillis": 0,
                "initSyncCrashRecoveryMillis": 0,
                "createLockFileMillis": 5,
                "getStorageEngineMetadataMillis": 0,
                "createStorageEngineMillis": 326,
                "writePIDMillis": 0,
                "writeNewMetadataMillis": 34,
                "initializeFCVForIndexMillis": 1,
                "dropAbandonedIdentsMillis": 0,
                "standaloneClusterParamsMillis": 0,
                "userAndRolesGraphMillis": 0,
                "waitForMajorityServiceMillis": 1,
                "startUpReplCoordMillis": 0,
                "recoverChangeStreamMillis": 0,
                "logStartupOptionsMillis": 0,
                "startUpTransportLayerMillis": 2,
                "initAndListenTotalMillis": 1014,
            },
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:47:41.267+05:30"},
    "s": "I",
    "c": "CONTROL",
    "id": 20712,
    "ctx": "LogicalSessionCacheReap",
    "msg": "Sessions collection is not set up; waiting until next sessions reap interval",
    "attr": {"error": "NamespaceNotFound: config.system.sessions does not exist"},
}
{
    "t": {"$date": "2025-11-23T02:47:41.267+05:30"},
    "s": "I",
    "c": "STORAGE",
    "id": 20320,
    "ctx": "LogicalSessionCacheRefresh",
    "msg": "createCollection",
    "attr": {
        "namespace": "config.system.sessions",
        "uuidDisposition": "generated",
        "uuid": {"uuid": {"$uuid": "30f92267-5122-41a9-8e68-98d0ead19005"}},
        "options": {},
    },
}
{
    "t": {"$date": "2025-11-23T02:47:41.284+05:30"},
    "s": "I",
    "c": "INDEX",
    "id": 20345,
    "ctx": "LogicalSessionCacheRefresh",
    "msg": "Index build: done building",
    "attr": {
        "buildUUID": null,
        "collectionUUID": {"uuid": {"$uuid": "30f92267-5122-41a9-8e68-98d0ead19005"}},
        "namespace": "config.system.sessions",
        "index": "_id_",
        "ident": "index-043df8c3-f8e9-4522-94ca-a997d3ff5f72",
        "collectionIdent": "collection-32e7a4e8-c357-49c6-ae3a-b23e3dd1a67d",
        "commitTimestamp": null,
    },
}
{
    "t": {"$date": "2025-11-23T02:47:41.284+05:30"},
    "s": "I",
    "c": "INDEX",
    "id": 20345,
    "ctx": "LogicalSessionCacheRefresh",
    "msg": "Index build: done building",
    "attr": {
        "buildUUID": null,
        "collectionUUID": {"uuid": {"$uuid": "30f92267-5122-41a9-8e68-98d0ead19005"}},
        "namespace": "config.system.sessions",
        "index": "lsidTTLIndex",
        "ident": "index-83a638c1-cf9e-4720-bbb8-8099f08372f3",
        "collectionIdent": "collection-32e7a4e8-c357-49c6-ae3a-b23e3dd1a67d",
        "commitTimestamp": null,
    },
}
{
    "t": {"$date": "2025-11-23T02:48:40.632+05:30"},
    "s": "I",
    "c": "WTCHKPT",
    "id": 22430,
    "ctx": "Checkpointer",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846320,
            "ts_usec": 632343,
            "thread": "2548:140730925155872",
            "session_name": "WT_SESSION.checkpoint",
            "category": "WT_VERB_CHECKPOINT_PROGRESS",
            "log_id": 1000000,
            "category_id": 7,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "saving checkpoint snapshot min: 33, snapshot max: 33 snapshot count: 0, oldest timestamp: (0, 0) , meta checkpoint timestamp: (0, 0) base write gen: 1",
        }
    },
}
{
    "t": {"$date": "2025-11-23T02:49:40.685+05:30"},
    "s": "I",
    "c": "WTCHKPT",
    "id": 22430,
    "ctx": "Checkpointer",
    "msg": "WiredTiger message",
    "attr": {
        "message": {
            "ts_sec": 1763846380,
            "ts_usec": 685053,
            "thread": "2548:140730925155872",
            "session_name": "WT_SESSION.checkpoint",
            "category": "WT_VERB_CHECKPOINT_PROGRESS",
            "log_id": 1000000,
            "category_id": 7,
            "verbose_level": "INFO",
            "verbose_level_id": 0,
            "msg": "saving checkpoint snapshot min: 35, snapshot max: 35 snapshot count: 0, oldest timestamp: (0, 0) , meta checkpoint timestamp: (0, 0) base write gen: 1",
        }
    },
}
try:
    from flasgger import Swagger

    _HAS_FLASGGER = True
except Exception:
    # Flasgger not available in the analyzer environment; proceed without Swagger UI
    Swagger = None
    _HAS_FLASGGER = False


app = Flask(__name__)

# Initialize Flasgger Swagger UI (only if available)
swagger_template = {
    "info": {
        "title": "Cardio Monitor API",
        "description": "API for uploading blood reports and heart readings from wearables and getting simple health analysis.",
        "version": "1.0.0",
    }
}
if _HAS_FLASGGER:
    Swagger(app, template=swagger_template)

# In-memory data store for uploaded readings
DATA_STORE = {}


def analyze_blood(blood):
    """Simple blood analysis logic (heuristic checks)."""
    issues = []
    # Example fields: hemoglobin, wbc, rbc, cholesterol, glucose
    hgb = blood.get("hemoglobin")
    if isinstance(hgb, (int, float)):
        if hgb < 12:
            issues.append("Low hemoglobin (possible anemia).")
        elif hgb > 17:
            issues.append("High hemoglobin.")
    chol = blood.get("cholesterol")
    if isinstance(chol, (int, float)) and chol > 200:
        issues.append("High cholesterol (risk for cardiovascular disease).")
    glucose = blood.get("glucose")
    if isinstance(glucose, (int, float)):
        if glucose >= 126:
            issues.append("High fasting glucose (possible diabetes).")
        elif glucose >= 100:
            issues.append("Elevated glucose (pre-diabetes).")
    wbc = blood.get("wbc")
    if isinstance(wbc, (int, float)) and wbc > 11000:
        issues.append("Elevated WBC (possible infection).")
    return issues


def analyze_heart(heart):
    """Simple heart reading analysis logic (blood pressure and heart rate)."""
    issues = []
    # Example fields: systolic, diastolic, heart_rate
    sys = heart.get("systolic")
    dia = heart.get("diastolic")
    hr = heart.get("heart_rate")
    if isinstance(sys, (int, float)) and isinstance(dia, (int, float)):
        if sys >= 140 or dia >= 90:
            issues.append("High blood pressure (hypertension).")
        elif sys < 90 or dia < 60:
            issues.append("Low blood pressure (hypotension).")
    if isinstance(hr, (int, float)):
        if hr > 100:
            issues.append("High heart rate (tachycardia).")
        elif hr < 50:
            issues.append("Low heart rate (bradycardia).")
    return issues


def save_reading(user_id, kind, payload):
    now = datetime.utcnow().isoformat() + "Z"
    analysis = analyze_blood(payload) if kind == "blood" else analyze_heart(payload)
    entry = {"data": payload, "analysis": analysis, "ts": now}
    DATA_STORE.setdefault(user_id, {})[kind] = entry
    return entry


def create_figure1(data1):
    fig = plt.subplots(figsize=(12, 8))
    barWidth = 0.25
    normal = data1[0]
    user = data1[1]
    br1 = np.arange(len(normal))
    br2 = [x + barWidth for x in br1]
    # br3 = [x + barWidth for x in br2]
    plt.bar(
        br1, normal, color="g", width=barWidth, edgecolor="grey", label="Normal Value"
    )
    plt.bar(br2, user, color="r", width=barWidth, edgecolor="grey", label="Yours Value")
    # plt.bar(br3, CSE, color ='b', width = barWidth, edgecolor ='grey', label ='CSE')
    plt.xlabel("Health status defining attributes", fontweight="bold", fontsize=15)
    plt.ylabel("respective values", fontweight="bold", fontsize=15)
    plt.xticks(
        [r + barWidth for r in range(len(normal))],
        ["cp", "chol", "fbs", "exang", "oldpeak", "slope", "ca", "thal"],
    )
    plt.legend()
    plt.savefig("static/plotng.png")


def create_figure2(data2):
    fig = plt.subplots(figsize=(12, 8))
    barWidth = 0.25
    normal = data2[0]
    user = data2[1]
    br1 = np.arange(len(normal))
    br2 = [x + barWidth for x in br1]
    plt.bar(
        br1, normal, color="g", width=barWidth, edgecolor="grey", label="Normal Value"
    )
    plt.bar(br2, user, color="r", width=barWidth, edgecolor="grey", label="Yours Value")
    plt.xlabel("Health status defining attributes", fontweight="bold", fontsize=15)
    plt.ylabel("respective values", fontweight="bold", fontsize=15)
    plt.xticks(
        [r + barWidth for r in range(len(normal))], ["trestbps", "chol", "thalach"]
    )
    plt.legend()
    plt.savefig("static/plotng2.png")


@app.route("/api/upload/blood", methods=["POST"])
def upload_blood():
    """
    Upload a blood report JSON and receive a quick analysis.
    ---
    tags:
      - Health API
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            user_id:
              type: string
            blood:
              type: object
              properties:
                hemoglobin:
                  type: number
                cholesterol:
                  type: number
                glucose:
                  type: number
                wbc:
                  type: number
    responses:
      200:
        description: Stored blood reading and analysis
      400:
        description: Invalid request
    """
    payload = request.get_json(force=True, silent=True)
    if not payload:
        return jsonify({"error": "Invalid or missing JSON"}), 400
    user_id = payload.get("user_id", "anonymous")
    blood = payload.get("blood")
    if not isinstance(blood, dict):
        return jsonify({"error": "Missing or invalid 'blood' object"}), 400
    entry = save_reading(user_id, "blood", blood)
    return jsonify({"status": "ok", "stored": entry}), 200


@app.route("/api/upload/heart", methods=["POST"])
def upload_heart():
    """
    Upload heart readings (from a watch/ring) and receive a quick analysis.
    ---
    tags:
      - Health API
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            user_id:
              type: string
            heart:
              type: object
              properties:
                systolic:
                  type: number
                diastolic:
                  type: number
                heart_rate:
                  type: number
    responses:
      200:
        description: Stored heart reading and analysis
      400:
        description: Invalid request
    """
    payload = request.get_json(force=True, silent=True)
    if not payload:
        return jsonify({"error": "Invalid or missing JSON"}), 400
    user_id = payload.get("user_id", "anonymous")
    heart = payload.get("heart")
    if not isinstance(heart, dict):
        return jsonify({"error": "Missing or invalid 'heart' object"}), 400
    entry = save_reading(user_id, "heart", heart)
    return jsonify({"status": "ok", "stored": entry}), 200


@app.route("/api/report/<user_id>", methods=["GET"])
def get_report(user_id):
    """
    Get latest combined report (blood + heart) for a user.
    ---
    tags:
      - Health API
    parameters:
      - name: user_id
        in: path
        type: string
        required: true
        description: User identifier
    responses:
      200:
        description: Combined report with analyses
      404:
        description: No data for user
    """
    user = DATA_STORE.get(user_id)
    if not user:
        return jsonify({"error": "No data for user"}), 404
    combined = {
        "blood": user.get("blood"),
        "heart": user.get("heart"),
        "summary": (
            user.get("blood", {}).get("analysis", [])
            + user.get("heart", {}).get("analysis", [])
        ),
    }
    return jsonify(combined), 200


@app.route("/")
def home():
    global counter2
    counter2 += 1
    return render_template("home.html", all_count=counter2)


global counter
counter = 0
global counter2
counter2 = 0


@app.route("/predict", methods=["POST"])
def predict():
    global data1
    global data2
    global counter
    global counter2
    if request.method == "POST":
        nameofpatient = request.form["name"]
        age = request.form["age"]
        sex = request.form["sex"]
        cp = request.form["cp"]
        trestbps = request.form["trestbps"]
        chol = request.form["chol"]
        fbs = request.form["fbs"]
        restecg = request.form["restecg"]
        thalach = request.form["thalach"]
        exang = request.form["exang"]
        oldpeak = request.form["oldpeak"]
        slope = request.form["slope"]
        ca = request.form["ca"]
        thal = request.form["thal"]
        counter += 1
        if counter <= 50:
            result = prediction.preprocess(
                age,
                sex,
                cp,
                trestbps,
                restecg,
                chol,
                fbs,
                thalach,
                exang,
                oldpeak,
                slope,
                ca,
                thal,
            )
        else:
            # modelbuild.bulidmodel()
            result = prediction.preprocess(
                age,
                sex,
                cp,
                trestbps,
                restecg,
                chol,
                fbs,
                thalach,
                exang,
                oldpeak,
                slope,
                ca,
                thal,
            )
            counter = 0
        # database.crudOperation(age,sex,cp,trestbps,restecg,chol,fbs,thalach,exang,oldpeak,slope,ca,thal,result)
        data1, data2 = visualization.visualizationpreprocess(
            age,
            sex,
            cp,
            trestbps,
            restecg,
            chol,
            fbs,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal,
            result,
        )
        create_figure1(data1)
        create_figure2(data2)
        return render_template(
            "result.html",
            prediction=result,
            nameofpatient=nameofpatient,
            model_counter=counter,
            total_counter=counter2,
        )


@app.route("/about")
def about():
    return render_template("disease.html")


@app.errorhandler(500)
def internal_error(error):

    return render_template("error.html")


@app.errorhandler(404)
def not_found(error):
    return "404 error", 404


if __name__ == "__main__":
    app.run(debug=True)
