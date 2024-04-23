from web3 import Web3
from web3.logs import DISCARD

SERENDALE_CONTRACT_ADDRESS = '0x0594D86b2923076a2316EaEA4E1Ca286dAA142C1'
CRYSTALVALE_CONTRACT_ADDRESS = '0xD507b6b299d9FC835a0Df92f718920D13fA49B47'
SERENDALE2_CONTRACT_ADDRESS = '0xdbEE8C336B06f2d30a6d2bB3817a3Ae0E34f4900'

ABI = """[
  {
    "anonymous": false,
    "inputs": [
      {
        "components": [
          {
            "internalType": "address",
            "name": "facetAddress",
            "type": "address"
          },
          {
            "internalType": "enum IDiamondCut.FacetCutAction",
            "name": "action",
            "type": "uint8"
          },
          {
            "internalType": "bytes4[]",
            "name": "functionSelectors",
            "type": "bytes4[]"
          }
        ],
        "indexed": false,
        "internalType": "struct IDiamondCut.FacetCut[]",
        "name": "_diamondCut",
        "type": "tuple[]"
      },
      {
        "indexed": false,
        "internalType": "address",
        "name": "_init",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "bytes",
        "name": "_calldata",
        "type": "bytes"
      }
    ],
    "name": "DiamondCut",
    "type": "event"
  },
  {
    "inputs": [
      {
        "components": [
          {
            "internalType": "address",
            "name": "facetAddress",
            "type": "address"
          },
          {
            "internalType": "enum IDiamondCut.FacetCutAction",
            "name": "action",
            "type": "uint8"
          },
          {
            "internalType": "bytes4[]",
            "name": "functionSelectors",
            "type": "bytes4[]"
          }
        ],
        "internalType": "struct IDiamondCut.FacetCut[]",
        "name": "_diamondCut",
        "type": "tuple[]"
      },
      {
        "internalType": "address",
        "name": "_init",
        "type": "address"
      },
      {
        "internalType": "bytes",
        "name": "_calldata",
        "type": "bytes"
      }
    ],
    "name": "diamondCut",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes4",
        "name": "_functionSelector",
        "type": "bytes4"
      }
    ],
    "name": "facetAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "facetAddress_",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "facetAddresses",
    "outputs": [
      {
        "internalType": "address[]",
        "name": "facetAddresses_",
        "type": "address[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_facet",
        "type": "address"
      }
    ],
    "name": "facetFunctionSelectors",
    "outputs": [
      {
        "internalType": "bytes4[]",
        "name": "facetFunctionSelectors_",
        "type": "bytes4[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "facets",
    "outputs": [
      {
        "components": [
          {
            "internalType": "address",
            "name": "facetAddress",
            "type": "address"
          },
          {
            "internalType": "bytes4[]",
            "name": "functionSelectors",
            "type": "bytes4[]"
          }
        ],
        "internalType": "struct IDiamondLoupe.Facet[]",
        "name": "facets_",
        "type": "tuple[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes4",
        "name": "_interfaceId",
        "type": "bytes4"
      }
    ],
    "name": "supportsInterface",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "previousOwner",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "newOwner",
        "type": "address"
      }
    ],
    "name": "OwnershipTransferred",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "owner",
    "outputs": [
      {
        "internalType": "address",
        "name": "owner_",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_newOwner",
        "type": "address"
      }
    ],
    "name": "transferOwnership",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "address",
        "name": "attunementCrystal",
        "type": "address"
      }
    ],
    "name": "AttunementCrystalAdded",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "feeAddress",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "feePercent",
        "type": "uint256"
      }
    ],
    "name": "FeeAddressAdded",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "source",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "from",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "address",
        "name": "token",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint64",
        "name": "timestamp",
        "type": "uint64"
      }
    ],
    "name": "FeeDeferred",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "source",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "from",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "address",
        "name": "token",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint64",
        "name": "timestamp",
        "type": "uint64"
      }
    ],
    "name": "FeeDisbursed",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "source",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "from",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "to",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "address",
        "name": "token",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint64",
        "name": "timestamp",
        "type": "uint64"
      }
    ],
    "name": "FeeLockedBurned",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "uint8",
        "name": "version",
        "type": "uint8"
      }
    ],
    "name": "Initialized",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "player",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "heroId",
        "type": "uint256"
      },
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "id",
            "type": "uint256"
          },
          {
            "components": [
              {
                "internalType": "uint256",
                "name": "summonedTime",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "nextSummonTime",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "summonerId",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "assistantId",
                "type": "uint256"
              },
              {
                "internalType": "uint32",
                "name": "summons",
                "type": "uint32"
              },
              {
                "internalType": "uint32",
                "name": "maxSummons",
                "type": "uint32"
              }
            ],
            "internalType": "struct SummoningInfo",
            "name": "summoningInfo",
            "type": "tuple"
          },
          {
            "components": [
              {
                "internalType": "uint256",
                "name": "statGenes",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "visualGenes",
                "type": "uint256"
              },
              {
                "internalType": "enum Rarity",
                "name": "rarity",
                "type": "uint8"
              },
              {
                "internalType": "bool",
                "name": "shiny",
                "type": "bool"
              },
              {
                "internalType": "uint16",
                "name": "generation",
                "type": "uint16"
              },
              {
                "internalType": "uint32",
                "name": "firstName",
                "type": "uint32"
              },
              {
                "internalType": "uint32",
                "name": "lastName",
                "type": "uint32"
              },
              {
                "internalType": "uint8",
                "name": "shinyStyle",
                "type": "uint8"
              },
              {
                "internalType": "uint8",
                "name": "class",
                "type": "uint8"
              },
              {
                "internalType": "uint8",
                "name": "subClass",
                "type": "uint8"
              }
            ],
            "internalType": "struct HeroInfo",
            "name": "info",
            "type": "tuple"
          },
          {
            "components": [
              {
                "internalType": "uint256",
                "name": "staminaFullAt",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "hpFullAt",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "mpFullAt",
                "type": "uint256"
              },
              {
                "internalType": "uint16",
                "name": "level",
                "type": "uint16"
              },
              {
                "internalType": "uint64",
                "name": "xp",
                "type": "uint64"
              },
              {
                "internalType": "address",
                "name": "currentQuest",
                "type": "address"
              },
              {
                "internalType": "uint8",
                "name": "sp",
                "type": "uint8"
              },
              {
                "internalType": "enum HeroStatus",
                "name": "status",
                "type": "uint8"
              }
            ],
            "internalType": "struct HeroState",
            "name": "state",
            "type": "tuple"
          },
          {
            "components": [
              {
                "internalType": "uint16",
                "name": "strength",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "intelligence",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "wisdom",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "luck",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "agility",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "vitality",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "endurance",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "dexterity",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "hp",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "mp",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "stamina",
                "type": "uint16"
              }
            ],
            "internalType": "struct HeroStats",
            "name": "stats",
            "type": "tuple"
          },
          {
            "components": [
              {
                "internalType": "uint16",
                "name": "strength",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "intelligence",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "wisdom",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "luck",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "agility",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "vitality",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "endurance",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "dexterity",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "hpSm",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "hpRg",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "hpLg",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "mpSm",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "mpRg",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "mpLg",
                "type": "uint16"
              }
            ],
            "internalType": "struct HeroStatGrowth",
            "name": "primaryStatGrowth",
            "type": "tuple"
          },
          {
            "components": [
              {
                "internalType": "uint16",
                "name": "strength",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "intelligence",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "wisdom",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "luck",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "agility",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "vitality",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "endurance",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "dexterity",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "hpSm",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "hpRg",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "hpLg",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "mpSm",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "mpRg",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "mpLg",
                "type": "uint16"
              }
            ],
            "internalType": "struct HeroStatGrowth",
            "name": "secondaryStatGrowth",
            "type": "tuple"
          },
          {
            "components": [
              {
                "internalType": "uint16",
                "name": "mining",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "gardening",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "foraging",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "fishing",
                "type": "uint16"
              }
            ],
            "internalType": "struct HeroProfessions",
            "name": "professions",
            "type": "tuple"
          }
        ],
        "indexed": false,
        "internalType": "struct Hero",
        "name": "hero",
        "type": "tuple"
      },
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "id",
            "type": "uint256"
          },
          {
            "components": [
              {
                "internalType": "uint256",
                "name": "summonedTime",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "nextSummonTime",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "summonerId",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "assistantId",
                "type": "uint256"
              },
              {
                "internalType": "uint32",
                "name": "summons",
                "type": "uint32"
              },
              {
                "internalType": "uint32",
                "name": "maxSummons",
                "type": "uint32"
              }
            ],
            "internalType": "struct SummoningInfo",
            "name": "summoningInfo",
            "type": "tuple"
          },
          {
            "components": [
              {
                "internalType": "uint256",
                "name": "statGenes",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "visualGenes",
                "type": "uint256"
              },
              {
                "internalType": "enum Rarity",
                "name": "rarity",
                "type": "uint8"
              },
              {
                "internalType": "bool",
                "name": "shiny",
                "type": "bool"
              },
              {
                "internalType": "uint16",
                "name": "generation",
                "type": "uint16"
              },
              {
                "internalType": "uint32",
                "name": "firstName",
                "type": "uint32"
              },
              {
                "internalType": "uint32",
                "name": "lastName",
                "type": "uint32"
              },
              {
                "internalType": "uint8",
                "name": "shinyStyle",
                "type": "uint8"
              },
              {
                "internalType": "uint8",
                "name": "class",
                "type": "uint8"
              },
              {
                "internalType": "uint8",
                "name": "subClass",
                "type": "uint8"
              }
            ],
            "internalType": "struct HeroInfo",
            "name": "info",
            "type": "tuple"
          },
          {
            "components": [
              {
                "internalType": "uint256",
                "name": "staminaFullAt",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "hpFullAt",
                "type": "uint256"
              },
              {
                "internalType": "uint256",
                "name": "mpFullAt",
                "type": "uint256"
              },
              {
                "internalType": "uint16",
                "name": "level",
                "type": "uint16"
              },
              {
                "internalType": "uint64",
                "name": "xp",
                "type": "uint64"
              },
              {
                "internalType": "address",
                "name": "currentQuest",
                "type": "address"
              },
              {
                "internalType": "uint8",
                "name": "sp",
                "type": "uint8"
              },
              {
                "internalType": "enum HeroStatus",
                "name": "status",
                "type": "uint8"
              }
            ],
            "internalType": "struct HeroState",
            "name": "state",
            "type": "tuple"
          },
          {
            "components": [
              {
                "internalType": "uint16",
                "name": "strength",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "intelligence",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "wisdom",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "luck",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "agility",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "vitality",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "endurance",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "dexterity",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "hp",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "mp",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "stamina",
                "type": "uint16"
              }
            ],
            "internalType": "struct HeroStats",
            "name": "stats",
            "type": "tuple"
          },
          {
            "components": [
              {
                "internalType": "uint16",
                "name": "strength",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "intelligence",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "wisdom",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "luck",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "agility",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "vitality",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "endurance",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "dexterity",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "hpSm",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "hpRg",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "hpLg",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "mpSm",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "mpRg",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "mpLg",
                "type": "uint16"
              }
            ],
            "internalType": "struct HeroStatGrowth",
            "name": "primaryStatGrowth",
            "type": "tuple"
          },
          {
            "components": [
              {
                "internalType": "uint16",
                "name": "strength",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "intelligence",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "wisdom",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "luck",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "agility",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "vitality",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "endurance",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "dexterity",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "hpSm",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "hpRg",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "hpLg",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "mpSm",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "mpRg",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "mpLg",
                "type": "uint16"
              }
            ],
            "internalType": "struct HeroStatGrowth",
            "name": "secondaryStatGrowth",
            "type": "tuple"
          },
          {
            "components": [
              {
                "internalType": "uint16",
                "name": "mining",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "gardening",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "foraging",
                "type": "uint16"
              },
              {
                "internalType": "uint16",
                "name": "fishing",
                "type": "uint16"
              }
            ],
            "internalType": "struct HeroProfessions",
            "name": "professions",
            "type": "tuple"
          }
        ],
        "indexed": false,
        "internalType": "struct Hero",
        "name": "oldHero",
        "type": "tuple"
      }
    ],
    "name": "LevelUp",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "player",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "heroId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "meditationId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint8",
        "name": "primaryStat",
        "type": "uint8"
      },
      {
        "indexed": false,
        "internalType": "uint8",
        "name": "secondaryStat",
        "type": "uint8"
      },
      {
        "indexed": false,
        "internalType": "uint8",
        "name": "tertiaryStat",
        "type": "uint8"
      },
      {
        "indexed": false,
        "internalType": "address",
        "name": "attunementCrystal",
        "type": "address"
      }
    ],
    "name": "MeditationBegun",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "player",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "heroId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "meditationId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint8",
        "name": "primaryStat",
        "type": "uint8"
      },
      {
        "indexed": false,
        "internalType": "uint8",
        "name": "secondaryStat",
        "type": "uint8"
      },
      {
        "indexed": false,
        "internalType": "uint8",
        "name": "tertiaryStat",
        "type": "uint8"
      },
      {
        "indexed": false,
        "internalType": "address",
        "name": "attunementCrystal",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint16",
        "name": "toLevel",
        "type": "uint16"
      }
    ],
    "name": "MeditationBegunWithLevel",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "player",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "heroId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "meditationId",
        "type": "uint256"
      }
    ],
    "name": "MeditationCompleted",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "player",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "heroId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "meditationId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "address",
        "name": "attunementCrystal",
        "type": "address"
      },
      {
        "indexed": false,
        "internalType": "uint16",
        "name": "toLevel",
        "type": "uint16"
      }
    ],
    "name": "MeditationCompletedV2",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "address",
        "name": "account",
        "type": "address"
      }
    ],
    "name": "Paused",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "bytes32",
        "name": "role",
        "type": "bytes32"
      },
      {
        "indexed": true,
        "internalType": "bytes32",
        "name": "previousAdminRole",
        "type": "bytes32"
      },
      {
        "indexed": true,
        "internalType": "bytes32",
        "name": "newAdminRole",
        "type": "bytes32"
      }
    ],
    "name": "RoleAdminChanged",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "bytes32",
        "name": "role",
        "type": "bytes32"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "account",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "sender",
        "type": "address"
      }
    ],
    "name": "RoleGranted",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "bytes32",
        "name": "role",
        "type": "bytes32"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "account",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "address",
        "name": "sender",
        "type": "address"
      }
    ],
    "name": "RoleRevoked",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "player",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "heroId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "stat",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint8",
        "name": "increase",
        "type": "uint8"
      },
      {
        "indexed": false,
        "internalType": "enum UpdateType",
        "name": "updateType",
        "type": "uint8"
      }
    ],
    "name": "StatUp",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "internalType": "address",
        "name": "player",
        "type": "address"
      },
      {
        "indexed": true,
        "internalType": "uint256",
        "name": "heroId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint256",
        "name": "stat",
        "type": "uint256"
      },
      {
        "indexed": false,
        "internalType": "uint16",
        "name": "increase",
        "type": "uint16"
      },
      {
        "indexed": false,
        "internalType": "enum UpdateType",
        "name": "updateType",
        "type": "uint8"
      },
      {
        "indexed": false,
        "internalType": "uint16",
        "name": "toLevel",
        "type": "uint16"
      }
    ],
    "name": "StatUpV2",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": false,
        "internalType": "address",
        "name": "account",
        "type": "address"
      }
    ],
    "name": "Unpaused",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "DEFAULT_ADMIN_ROLE",
    "outputs": [
      {
        "internalType": "bytes32",
        "name": "",
        "type": "bytes32"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "MODERATOR_ROLE",
    "outputs": [
      {
        "internalType": "bytes32",
        "name": "",
        "type": "bytes32"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "name": "activeAttunementCrystals",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_address",
        "type": "address"
      }
    ],
    "name": "addAttunementCrystal",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_heroId",
        "type": "uint256"
      }
    ],
    "name": "adminRemove",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "feeAddresses",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "feePercents",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "role",
        "type": "bytes32"
      }
    ],
    "name": "getRoleAdmin",
    "outputs": [
      {
        "internalType": "bytes32",
        "name": "",
        "type": "bytes32"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "role",
        "type": "bytes32"
      },
      {
        "internalType": "address",
        "name": "account",
        "type": "address"
      }
    ],
    "name": "grantRole",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "role",
        "type": "bytes32"
      },
      {
        "internalType": "address",
        "name": "account",
        "type": "address"
      }
    ],
    "name": "hasRole",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "heroToMeditation",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "pause",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "paused",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "powerToken",
    "outputs": [
      {
        "internalType": "contract IPowerToken",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "profileActiveMeditations",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "id",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "player",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "heroId",
        "type": "uint256"
      },
      {
        "internalType": "uint8",
        "name": "primaryStat",
        "type": "uint8"
      },
      {
        "internalType": "uint8",
        "name": "secondaryStat",
        "type": "uint8"
      },
      {
        "internalType": "uint8",
        "name": "tertiaryStat",
        "type": "uint8"
      },
      {
        "internalType": "address",
        "name": "attunementCrystal",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "startBlock",
        "type": "uint256"
      },
      {
        "internalType": "uint8",
        "name": "status",
        "type": "uint8"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_address",
        "type": "address"
      }
    ],
    "name": "removeAttunementCrystal",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "role",
        "type": "bytes32"
      },
      {
        "internalType": "address",
        "name": "account",
        "type": "address"
      }
    ],
    "name": "renounceRole",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "role",
        "type": "bytes32"
      },
      {
        "internalType": "address",
        "name": "account",
        "type": "address"
      }
    ],
    "name": "revokeRole",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "name": "runes",
    "outputs": [
      {
        "internalType": "contract IInventoryItem",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address[]",
        "name": "_feeAddresses",
        "type": "address[]"
      },
      {
        "internalType": "uint256[]",
        "name": "_feePercents",
        "type": "uint256[]"
      }
    ],
    "name": "setFees",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_flagStorageAddress",
        "type": "address"
      }
    ],
    "name": "setFlagStorage",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_powerTokenAddress",
        "type": "address"
      }
    ],
    "name": "setPowerToken",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_randomGeneratorAddress",
        "type": "address"
      }
    ],
    "name": "setRandomGenerator",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint8",
        "name": "_index",
        "type": "uint8"
      },
      {
        "internalType": "address",
        "name": "_address",
        "type": "address"
      }
    ],
    "name": "setRune",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_statScienceAddress",
        "type": "address"
      }
    ],
    "name": "setStatScienceAddress",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_tokenUnlockerAddress",
        "type": "address"
      }
    ],
    "name": "setTokenUnlocker",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "tokenUnlockerAddress",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "unpause",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_heroId",
        "type": "uint256"
      }
    ],
    "name": "completeMeditation",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256[]",
        "name": "_heroIds",
        "type": "uint256[]"
      }
    ],
    "name": "completeMeditations",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_address",
        "type": "address"
      }
    ],
    "name": "getActiveMeditations",
    "outputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "id",
            "type": "uint256"
          },
          {
            "internalType": "address",
            "name": "player",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "heroId",
            "type": "uint256"
          },
          {
            "internalType": "uint8",
            "name": "primaryStat",
            "type": "uint8"
          },
          {
            "internalType": "uint8",
            "name": "secondaryStat",
            "type": "uint8"
          },
          {
            "internalType": "uint8",
            "name": "tertiaryStat",
            "type": "uint8"
          },
          {
            "internalType": "address",
            "name": "attunementCrystal",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "startBlock",
            "type": "uint256"
          },
          {
            "internalType": "uint8",
            "name": "status",
            "type": "uint8"
          }
        ],
        "internalType": "struct Meditation[]",
        "name": "",
        "type": "tuple[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_heroId",
        "type": "uint256"
      }
    ],
    "name": "getHeroMeditation",
    "outputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "id",
            "type": "uint256"
          },
          {
            "internalType": "address",
            "name": "player",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "heroId",
            "type": "uint256"
          },
          {
            "internalType": "uint8",
            "name": "primaryStat",
            "type": "uint8"
          },
          {
            "internalType": "uint8",
            "name": "secondaryStat",
            "type": "uint8"
          },
          {
            "internalType": "uint8",
            "name": "tertiaryStat",
            "type": "uint8"
          },
          {
            "internalType": "address",
            "name": "attunementCrystal",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "startBlock",
            "type": "uint256"
          },
          {
            "internalType": "uint8",
            "name": "status",
            "type": "uint8"
          }
        ],
        "internalType": "struct Meditation",
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_id",
        "type": "uint256"
      }
    ],
    "name": "getMeditation",
    "outputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "id",
            "type": "uint256"
          },
          {
            "internalType": "address",
            "name": "player",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "heroId",
            "type": "uint256"
          },
          {
            "internalType": "uint8",
            "name": "primaryStat",
            "type": "uint8"
          },
          {
            "internalType": "uint8",
            "name": "secondaryStat",
            "type": "uint8"
          },
          {
            "internalType": "uint8",
            "name": "tertiaryStat",
            "type": "uint8"
          },
          {
            "internalType": "address",
            "name": "attunementCrystal",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "startBlock",
            "type": "uint256"
          },
          {
            "internalType": "uint8",
            "name": "status",
            "type": "uint8"
          }
        ],
        "internalType": "struct Meditation",
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint16",
        "name": "_level",
        "type": "uint16"
      }
    ],
    "name": "_getRequiredRunes",
    "outputs": [
      {
        "internalType": "uint16[10]",
        "name": "",
        "type": "uint16[10]"
      }
    ],
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_heroId",
        "type": "uint256"
      },
      {
        "internalType": "uint8",
        "name": "_primaryStat",
        "type": "uint8"
      },
      {
        "internalType": "uint8",
        "name": "_secondaryStat",
        "type": "uint8"
      },
      {
        "internalType": "uint8",
        "name": "_tertiaryStat",
        "type": "uint8"
      },
      {
        "internalType": "address",
        "name": "_attunementCrystal",
        "type": "address"
      }
    ],
    "name": "startMeditation",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_heroId",
        "type": "uint256"
      },
      {
        "internalType": "uint8",
        "name": "_primaryStat",
        "type": "uint8"
      },
      {
        "internalType": "uint8",
        "name": "_secondaryStat",
        "type": "uint8"
      },
      {
        "internalType": "uint8",
        "name": "_tertiaryStat",
        "type": "uint8"
      },
      {
        "internalType": "address",
        "name": "_attunementCrystal",
        "type": "address"
      }
    ],
    "name": "startMeditationWithLocked",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "heroId",
            "type": "uint256"
          },
          {
            "internalType": "uint8",
            "name": "primaryStat",
            "type": "uint8"
          },
          {
            "internalType": "uint8",
            "name": "secondaryStat",
            "type": "uint8"
          },
          {
            "internalType": "uint8",
            "name": "tertiaryStat",
            "type": "uint8"
          },
          {
            "internalType": "address",
            "name": "attunementCrystal",
            "type": "address"
          },
          {
            "internalType": "bool",
            "name": "useLockedTokens",
            "type": "bool"
          }
        ],
        "internalType": "struct MeditationInput[]",
        "name": "_meditations",
        "type": "tuple[]"
      }
    ],
    "name": "startMeditations",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  }
]
    """

ZERO_ADDRESS = '0x0000000000000000000000000000000000000000'


def block_explorer_link(contract_address, txid):
    if hasattr(contract_address, 'address'):
        contract_address = str(contract_address.address)
    contract_address = str(contract_address).upper()
    if contract_address == SERENDALE_CONTRACT_ADDRESS.upper():
        return 'https://explorer.harmony.one/tx/' + str(txid)
    elif contract_address == CRYSTALVALE_CONTRACT_ADDRESS.upper():
        return 'https://subnets.avax.network/defi-kingdoms/dfk-chain/explorer/tx/' + str(txid)
    elif contract_address == SERENDALE2_CONTRACT_ADDRESS.upper():
        return 'https://scope.klaytn.com/tx/' + str(txid)
    else:
        return str(txid)


def get_required_runes(contract_address, level, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions._getRequiredRunes(level).call()


def active_attunement_crystals(contract_address, address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.activeAttunementCrystals(address).call()


def add_attunement_crystal(contract_address, address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.addAttunementCrystal(address).call()


def start_meditation(contract_address, hero_id, trait1, trait2, trait3, attunement_crystal_address, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):

    if type(trait1) == str:
        trait1 = trait2id(trait1)

    if type(trait2) == str:
        trait2 = trait2id(trait2)

    if type(trait3) == str:
        trait3 = trait2id(trait3)

    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.from_key(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.startMeditation(hero_id, trait1, trait2, trait3, attunement_crystal_address)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.build_transaction(
            {'maxFeePerGas': w3.to_wei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.to_wei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.build_transaction({'gasPrice': w3.to_wei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info("Waiting for transaction " + block_explorer_link(contract_address, signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt


def complete_meditation(contract_address, hero_id, private_key, nonce, gas_price_gwei, tx_timeout_seconds, rpc_address, logger):
    w3 = Web3(Web3.HTTPProvider(rpc_address))
    account = w3.eth.account.from_key(private_key)
    w3.eth.default_account = account.address

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    tx = contract.functions.completeMeditation(hero_id)

    if isinstance(gas_price_gwei, dict):  # dynamic fee
        tx = tx.build_transaction(
            {'maxFeePerGas': w3.to_wei(gas_price_gwei['maxFeePerGas'], 'gwei'),
             'maxPriorityFeePerGas': w3.to_wei(gas_price_gwei['maxPriorityFeePerGas'], 'gwei'), 'nonce': nonce})
    else:  # legacy
        tx = tx.build_transaction({'gasPrice': w3.to_wei(gas_price_gwei, 'gwei'), 'nonce': nonce})

    logger.debug("Signing transaction")
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    logger.debug("Sending transaction " + str(tx))
    ret = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    logger.debug("Transaction successfully sent !")
    logger.info("Waiting for transaction " + block_explorer_link(contract_address, signed_tx.hash.hex()) + " to be mined")
    tx_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash=signed_tx.hash, timeout=tx_timeout_seconds,
                                                     poll_latency=2)
    logger.info("Transaction mined !")

    return tx_receipt


def parse_meditation_results(contract_address, tx_receipt, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    meditation_result = {}
    level_up = contract.events.LevelUp().process_receipt(tx_receipt, errors=DISCARD)
    new_level = level_up[0]['args']["hero"][3][3]
    
    stat_up = contract.events.StatUpV2().process_receipt(tx_receipt, errors=DISCARD)

    hero_id = None
    for stat in stat_up:
        hero_id = stat['args']['heroId']

        if hero_id not in meditation_result:
            meditation_result[hero_id] = {}
        
        if not id2stat(stat['args']['stat']) in meditation_result[hero_id]:
            meditation_result[hero_id][id2stat(stat['args']['stat'])] = {"increase": 0}

        meditation_result[hero_id][id2stat(stat['args']['stat'])]["increase"] += stat['args']['increase']

    if hero_id:
        meditation_result[hero_id]["new level"] = new_level
    
    return meditation_result


def get_active_meditations(contract_address, address, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.getActiveMeditations(address).call()


def get_hero_meditation(contract_address, hero_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    result = contract.functions.getHeroMeditation(hero_id).call()
    if result[0] == 0:
        return None
    return result


def get_meditation(contract_address, meditation_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    result = contract.functions.getMeditation(meditation_id).call()
    if result[0] == 0:
        return None
    return result


def hero_to_meditation_id(contract_address, hero_id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.heroToMeditation(hero_id).call()


def profile_active_meditations(contract_address, address, id, rpc_address):
    w3 = Web3(Web3.HTTPProvider(rpc_address))

    contract_address = Web3.to_checksum_address(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)

    return contract.functions.profileActiveMeditations(address, id).call()


def trait2id(label):
    stats = {
        'strength': 0,
        'agility': 1,
        'intelligence': 2,
        'wisdom': 3,
        'luck': 4,
        'vitality': 5,
        'endurance': 6,
        'dexterity': 7
    }
    return stats.get(label, None)


def id2stat(label):
    stats = {
        0: 'STR',
        1: 'AGI',
        2: 'INT',
        3: 'WIS',
        4: 'LCK',
        5: 'VIT',
        6: 'END',
        7: 'DEX',
        8: 'HP',
        9: 'MP',
        10: 'STAMINA'
    }
    return stats.get(label, None)


def xp_per_level(level):
    next_level = level + 1
    if level < 6:
        return next_level * 1000
    elif level < 9:
        return 4000 + (next_level - 5) * 2000
    elif level < 16:
        return 12000 + (next_level - 9) * 4000
    elif level < 36:
        return 40000 + (next_level - 16) * 5000
    elif level < 56:
        return 140000 + (next_level - 36) * 7500
    else:
        return 290000 + (next_level - 56) * 10000
