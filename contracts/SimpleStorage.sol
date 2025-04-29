
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {

    // comment
    uint256 public favoriteNumber;

    struct People{
        uint256 favoriteNumber;
        string name;
        
    //People public person = People({favoriteNumber: 2, name: "Patrick"});
        
    }

    People[] public people;
    mapping(string => uint256) public NameToFavoriteNumber;

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        //People memory _person = People({favoriteNumber: _favoriteNumber, name: _name});
        people.push(People({favoriteNumber: _favoriteNumber, name: _name}));
        //mapping (string => uint256) storage _storage = NameToFavoriteNumber;
        NameToFavoriteNumber[_name] = _favoriteNumber;  
    }

   

    function store(uint256 _favoriteNumber) public returns(uint256) {
        favoriteNumber = _favoriteNumber;
        return _favoriteNumber;
    }

    function retrieve() public view returns (uint256){
        return favoriteNumber*2;
    }

    function retrieve2(uint256 favoriteNumber) public pure returns(uint256) {
         return favoriteNumber*2;
    }


}


