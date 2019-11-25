{
  "targets": [
    {
      "target_name": "desktopIdle",
      "sources": [
        "src/desktop_idle.cc"
      ],
      "conditions": [
        ['OS=="mac"', {
          "sources": [
            "src/mac/idle.mm"
          ],
          "xcode_settings": {
            "OTHER_LDFLAGS": ["-framework CoreGraphics"]
          }
        }],
        [
          'OS=="linux"',
          {
            "sources": [
              "src/linux/idle.cc"
            ],
            "variables": {
	            "pkg-config": "pkg-config"
            },
            "sources": [
              "src/linux/idle.cc"
            ],
            "direct_dependent_settings": {
              "cflags": [
                "<!@(<(pkg-config) --cflags x11 xext xscrnsaver)",
              ],
            },
            "link_settings": {
              "ldflags": [
                "<!@(<(pkg-config) --libs-only-other --libs-only-L x11 xext xscrnsaver)",
              ],
              "libraries": [
                "<!@(<(pkg-config) --libs-only-l x11 xext xscrnsaver)",
              ]
            }
          }
        ],
        [
          'OS=="freebsd"',
          {
            "sources": [
              "src/linux/idle.cc"
            ],
            "variables": {
	            "pkg-config": "pkg-config"
            },
            "sources": [
              "src/linux/idle.cc"
            ],
	    "include_dirs": [
		"/usr/local/include"
	    ],
            "direct_dependent_settings": {
              "cflags": [
                "<!@(<(pkg-config) --cflags x11 xext xscrnsaver)",
              ],
            },
            "link_settings": {
              "ldflags": [
                "<!@(<(pkg-config) --libs-only-other --libs-only-L x11 xext xscrnsaver)",
              ],
              "libraries": [
                "<!@(<(pkg-config) --libs-only-l x11 xext xscrnsaver)",
              ]
            }
          }
        ],
        [
          'OS=="openbsd"',
          {
            "sources": [
              "src/linux/idle.cc"
            ],
            "variables": {
	            "pkg-config": "pkg-config"
            },
            "sources": [
              "src/linux/idle.cc"
            ],
	    "include_dirs": [
		"/usr/X11R6/include"
	    ],
            "direct_dependent_settings": {
              "cflags": [
                "<!@(<(pkg-config) --cflags x11 xext xscrnsaver)",
              ],
            },
            "link_settings": {
              "ldflags": [
                "<!@(<(pkg-config) --libs-only-other --libs-only-L x11 xext xscrnsaver)",
              ],
              "libraries": [
                "<!@(<(pkg-config) --libs-only-l x11 xext xscrnsaver)",
              ]
            }
          }
        ],
	[
          'OS=="win"',
          {
            "sources": [
              "src/win/idle.cc"
            ],
            "msvs_settings": {
              "VCLinkerTool": {
                # Don't print a linker warning when no imports from either .exe are used.
                "AdditionalOptions": ["/ignore:4199"],
              }
            }
          }
        ]
      ]
    }
  ]
}
