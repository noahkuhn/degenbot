from typing import List

import eth_abi.packed
from web3 import Web3


def generate_v2_pool_address(
    token_addresses: List[str],
    factory_address: str,
    init_hash: str,
) -> str:
    """
    Generate the deterministic pool address from the token addresses.

    Adapted from https://github.com/Uniswap/universal-router/blob/deployed-commit/contracts/modules/uniswap/v2/UniswapV2Library.sol
    """

    token_addresses = sorted([address.lower() for address in token_addresses])

    return Web3.toChecksumAddress(
        Web3.keccak(
            hexstr="0xff"
            + factory_address[2:]
            + Web3.keccak(
                eth_abi.packed.encode_packed(
                    ["address", "address"],
                    [*token_addresses],
                )
            ).hex()[2:]
            + init_hash[2:]
        )[12:]
    )
