from setuptools import setup

dependencies = [
    "blspy==1.0.5",  # Signature library
    "chiavdf==1.0.2",  # timelord and vdf verification
    "chiabip158==1.0",  # bip158-style wallet filters
    "chiapos==1.0.4",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.14",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.7",  # Binary data management library
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the cannabis processes readable names
    "sortedcontainers==2.3.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspython==2.1.0",  # Query DNS seeds
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
]

kwargs = dict(
    name="cannabis-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@cannabischain.net",
    description="Chia blockchain full node, farmer, timelord, and wallet.",
    url="https://chia.net/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="chia blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "cannabis",
        "cannabis.cmds",
        "cannabis.clvm",
        "cannabis.consensus",
        "cannabis.daemon",
        "cannabis.full_node",
        "cannabis.timelord",
        "cannabis.farmer",
        "cannabis.harvester",
        "cannabis.introducer",
        "cannabis.plotting",
        "cannabis.pools",
        "cannabis.protocols",
        "cannabis.rpc",
        "cannabis.server",
        "cannabis.simulator",
        "cannabis.types.blockchain_format",
        "cannabis.types",
        "cannabis.util",
        "cannabis.wallet",
        "cannabis.wallet.puzzles",
        "cannabis.wallet.rl_wallet",
        "cannabis.wallet.cc_wallet",
        "cannabis.wallet.did_wallet",
        "cannabis.wallet.settings",
        "cannabis.wallet.trading",
        "cannabis.wallet.util",
        "cannabis.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "cannabis = cannabis.cmds.cannabis:main",
            "cannabis_wallet = cannabis.server.start_wallet:main",
            "cannabis_full_node = cannabis.server.start_full_node:main",
            "cannabis_harvester = cannabis.server.start_harvester:main",
            "cannabis_farmer = cannabis.server.start_farmer:main",
            "cannabis_introducer = cannabis.server.start_introducer:main",
            "cannabis_timelord = cannabis.server.start_timelord:main",
            "cannabis_timelord_launcher = cannabis.timelord.timelord_launcher:main",
            "cannabis_full_node_simulator = cannabis.simulator.start_simulator:main",
        ]
    },
    package_data={
        "cannabis": ["pyinstaller.spec"],
        "": ["*.clvm", "*.clvm.hex", "*.clib", "*.clinc", "*.clsp"],
        "cannabis.util": ["initial-*.yaml", "english.txt"],
        "cannabis.ssl": ["cannabis_ca.crt", "cannabis_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
