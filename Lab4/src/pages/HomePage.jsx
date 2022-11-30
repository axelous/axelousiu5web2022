import {UserCard} from "../components/UserCard";
import {users} from "../mocks";
import {Link} from "react-router-dom";

export const HomePage = () =>{
    return (
        <div>
            <Link to="/">Главная</Link>
            <p>
                {users.map(user=><UserCard key={user.idUser} {...user}/>)}
            </p>
        </div>
    )
}