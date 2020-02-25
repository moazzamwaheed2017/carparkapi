import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { FindRouteModel } from "../models/findroute.model";
import { Observable } from "rxjs/index";
import { ApiResponse } from "../models/api.response";

@Injectable()
export class FindRouteApi {

    constructor(private http: HttpClient) { }
    baseUrl: string = 'http://localhost:50224/FindByParkingApi';

    getMap(): Observable<ApiResponse> {
        return this.http.get<ApiResponse>(this.baseUrl);
    }
}
