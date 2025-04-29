

// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./SimpleStorage.sol";

contract StorageFactory is SimpleStorage {
    SimpleStorage[] public simpleStorageArray;
    function createSimpleStorageContract() public {
        SimpleStorage simpleStorage = new SimpleStorage();
        simpleStorageArray.push(simpleStorage);
    }
    function sfStore(uint256 _simpleStorageIndex, uint256 _simplestorageNumber) public{
        // A ddress
        //ABI
        SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        simpleStorage.store(_simplestorageNumber);
    }
    function sfGet(uint256 _simpleStorageIndex) public view returns(uint256){
        SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_simpleStorageIndex]));
        return simpleStorage.retrieve();
        
    }

    // function getNumberOfStorages() public view returns (uint256) {
    //     return simpleStorageArray.length;
    //} 
 


}